#!/usr/bin/python3
import argparse, textwrap
import os, sys
import PTCFile

##
##

SCRIPTDIR = os.path.dirname(__file__)
prgerr=False
argpar = argparse.ArgumentParser(description="Manage SmileBASIC 3/4 files", exit_on_error=False)

arggp0=argpar.add_argument_group("Files")
arggp0.add_argument("file", type=str, metavar="file", help='Input file')
arggp0.add_argument("-o", metavar="outf", type=str, help='Output file (if omitted, writing copy in "out" folder)')

arggp1 = argpar.add_argument_group("Common arguments","The following arguments can be used for most file formats")
arggp1.add_argument("-s", "--stats", action="store_true", help='Show information about the input file')
arggp1.add_argument("-c", "--compress", action="store_true", help="Apply compression (if none was applied)")
arggp1.add_argument("-d", "--decompress", action="store_true", help="Remove compression (if it was applied)")
arggp1.add_argument("-e", "--extract", metavar="fmt", nargs="*", help='Extract the data from the file (see "-e help" for supported formats)')
arggp1.add_argument("-v", "--verify", action="store_true", help="Check, if the input file is valid.")
arggp1.add_argument("--fix", metavar="level", nargs="*", help="Attempt to fix a bad file. (See --fix help for level)")

arggp2 = argpar.add_argument_group("DAT files")
arggp2.add_argument("-g", "--optimize", action="store_true", help="Look for optimizations and apply them")

arggp3 = argpar.add_argument_group("Project files")
arggp3.add_argument("--prj-pack", action="store_true", help="Pack a project folder into a project file")
arggp3.add_argument("--prj-unpack", action="store_true", help="Unpack files from the project file")

arggp4 = argpar.add_argument_group("SmileBASIC 4 Metadata")
arggp4.add_argument("--make-meta", metavar=("prjName","prjDescription","iconFile"), nargs=3, help="Build a META file")
arggp4.add_argument("--get-meta", metavar="property", nargs="*", help="Get a property from a META file (see --get-meta help)")

args = argpar.parse_args()
try:
	if args.compress and args.decompress: raise argparse.ArgumentError(None, "Contradicting arguments: -c/--compress and -d/--decompress")
	
	inFileStm = open(args.file,"rb")
	inFileStm.seek(0,0)
	origfobj = PTCFile.File(inFileStm)
	origf = origfobj.format
	inFileStm.close()
	szDiff = origf.getDataSize() - origf.head.dataSize
	if origf.error: raise TypeError("File failed to parse: "+origf.errorstr)
	if args.stats:
		print(textwrap.dedent('''\
			File header of %s:
			
			  File type: %s made for SmileBASIC %d
			  Data size: %d %s %s
			  Modified: %s, %d/%d/%d at %d:%02d:%02d
			  Created by: %s (ID: 0x%X, 0x%X)
			  Uploaded by: %s (ID: 0x%X, 0x%X)
		''' % (\
		args.file, origf.head.getFileTypeName(),\
		origf.head.isForSwitch()+3, origf.head.dataSize, \
		"(desynced: {} B)".format(szDiff)*(szDiff != 0),\
		"(compressed)"*(origf.head.compress != 0),\
		origf.head.getWeekdayStr(), origf.head.modYear, origf.head.modMonth, \
		origf.head.modDay, origf.head.modHour, origf.head.modMinute, \
		origf.head.modSecond, origf.head.creatorName, origf.head.creatorID, \
		origf.head.creator_uploadID, origf.head.uploaderName, \
		origf.head.uploaderID, origf.head.uploader_uploadID
		)))
	if args.verify and origf.valid:
		print("File is valid")
	if args.verify and not origf.valid:
		print("File is not valid; bad checksum or bad content for specified file type"); prgerr=True
	try: args.extract.index("help")
	except: pass
	else:
		print(textwrap.dedent("""\
			About File Content Extraction

			You can specify multiple arguments to extract specific elements.

			Types are specified in the following structure:
				filePart:value:outFile
			
			
			filePart: The part of a file you want to extract an element from
				head   - File header information
				subhdr - Secondary header (SB3/SB4-only, for DAT,GRP,META,PRJ)
				data   - Main data
			
			value: A specific value (or element) to extract

			outFile: Output file name for extracted elements
				The output format often depends on the file extension used.
			
			See {} {} -e types for supported extraction options
		""".format(sys.argv[0],args.file)))
	try: args.extract.index("types")
	except: pass
	else:
		print("Supported extraction options for {}:".format(args.file))
		print("\n  Header (head):")
		k = 0
		if hasattr(origf.head,"extractables"):
			extup=origf.head.extractables(); j=""; k += 1
			for i in extup: j += i + ", "
			print("   Elements: {}".format(j[:-2]))
		if hasattr(origf.head,"extractFmt"):
			extup=origf.head.extractFmt(); j=""; k += 1
			for i in extup: j += i + ", "
			print("   Savable as: {}".format(j[:-2]))
		if k < 1: print("   (no extractable elements or output formats)")
		k = 0
		if origf.neck != None:
			print("\n  Secondary header (subhdr):")
			if hasattr(origf.neck,"extractables"):
				extup=origf.neck.extractables(); j=""; k += 1
				for i in extup: j += i + ", "
				print("   Elements: {}".format(j[:-2]))
			if hasattr(origf.neck,"extractFmt"):
				extup=origf.neck.extractFmt(); j=""; k += 1
				for i in extup: j += i + ", "
				print("   Savable as: {}".format(j[:-2]))
			if k < 1: print("   (no extractable elements or output formats)")
		k = 0
		print("\n  Data section (data):")
		if hasattr(origf.data,"extractables"):
			extup=origf.data.extractables(); j=""; k += 1
			for i in extup: j += i + ", "
			print("   Elements: {}".format(j[:-2]))
		if hasattr(origf.data,"extractFmt"):
			extup=origf.data.extractFmt(); j=""; k += 1
			for i in extup: j += i + ", "
			print("   Savable as: {}".format(j[:-2]))
		if k < 1:
			print("   (no extractable elements or output formats)")
	print("\nPlease note that this tool is just getting started. I have only made the basics here.\n")

except:
	errtype, errvalue, errtrace = sys.exc_info()
	if errtype!=SystemExit:
		#print("\n An error has occured while running the script.\n")
		#traceback.print_exception(errtype, errvalue, errtrace)
		print("\n An exception occured (%s):\n  %s\n" % (str(errtype).split("'")[1],str(errvalue)))
		prgerr=True

exit(prgerr)