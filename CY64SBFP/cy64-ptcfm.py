#!/usr/bin/python3
import argparse, textwrap
import os, sys, traceback
import PTCFile
from stat import *
from glob import *
from PTCFile.Helper import mkfolders
import PTCFile.PRJMake as prj
SCRIPTDIR = os.path.dirname(__file__)
prgerr=False
argpar = argparse.ArgumentParser(description="Manage SmileBASIC 3/4 files", exit_on_error=False)

argpar.add_argument("-i", "--input", metavar="file", help='Input file (required)')
argpar.add_argument("-o", "--output", metavar="file", help='Output file (required for -e)')
argpar.add_argument("-s", "--stats", action="store_true", help='Show information about the input file')
argpar.add_argument("-c", "--compress", action="store_true", help="Apply compression (if none was applied)")
argpar.add_argument("-d", "--decompress", action="store_true", help="Remove compression (if it was applied)")
argpar.add_argument("-e", "--extract", action="store_true", help='Extract the file contents into a folder')
argpar.add_argument("-v", "--verify", action="store_true", help="Check, if the input file is valid.")
argpar.add_argument("-u", "--update", action="store_true", help="Update file header")
argpar.add_argument("-0", "--setname", metavar="name", help="Set creator/editor name")
argpar.add_argument("--bulk", action="store_true", help="(Internal use) Silent mode")

args = argpar.parse_args()
# print(args)
#try:
if True:
  if args.compress and args.decompress: raise argparse.ArgumentError(None, "Cannot compress and decompress simultaneously; what the heck?")
  if (args.compress or args.decompress) and args.extract: raise argparse.ArgumentError(None, "Cannot (de-)compress and extract simulataneously.")
  if type(args.output)!=str and args.extract:
    raise argparse.ArgumentError(None, "No output name provided, try specifying a folder or file with -o")

  if args.setname and len(args.setname)>16:
    raise argparse.ArgumentError(None, "The user name you specified is too long.")

  if type(args.input)!=str:
    raise argparse.ArgumentError(None, "No input provided, try specifying a folder or file with -i")
  elif S_ISDIR(os.stat(args.input).st_mode):
    l=glob(args.input+"/*")
    a=sys.argv; b=""
    for i in a:
      if i==args.input: b += "\"{}\" "
      else: b += i+" "
    try: a.index("--bulk")
    except: b += " --bulk"
    if args.bulk:
      print(" --- Entered new folder: %s"%args.input)
    else:
      print("Folder specified as input; recursively reading inner files...")
    for i in range(len(l)):
      print("(% 5.1f%%) %s ..." % ((i/(len(l)-1)*100), l[i]))
      if os.system(b.format(l[i]))>0: exit(1)
  else:
    flushFile = False
    inFileStm = open(args.input,"rb")
    inFileStm.seek(0,0)
    origfobj = PTCFile.File(inFileStm)
    origf = origfobj.format
    inFileStm.close()
    szDiff = origf.getDataSize() - origf.head.dataSize
    #if origf.error: raise TypeError("File failed to parse: "+origf.errorstr)
    if args.stats:
      print(textwrap.dedent('''\
        File header of %s:
          File type : %s for SB%d (%s)
          Data size : %d bytes %s%s
          Modified  : %s, %04d/%d/%d at %d:%02d:%02d
          Creator   : "%s" (ID: 0x%08X)
          Editor    : "%s" (ID: 0x%08X)
      ''' % (\
      args.input, origf.head.getFileTypeName(),\
      origf.head.isForSwitch()+3, str(type(origf.fmt)).split("'")[1].split(".")[-1],\
      origf.head.dataSize,\
      "(desynced: {} B) ".format(szDiff)*(szDiff != 0 and origf.head.getFileTypeName()!="PRJ"),\
      "(compressed)"*(origf.head.compress != 0),\
      origf.head.getWeekdayStr(), origf.head.modYear, origf.head.modMonth, \
      origf.head.modDay, origf.head.modHour, origf.head.modMinute, \
      origf.head.modSecond, origf.head.creatorName, origf.head.creatorID, \
      origf.head.uploaderName, origf.head.uploaderID
      )))
    if args.verify:
      if not origf.usesHash():
        print("Cannot check validity, as the file's type doesn't use a integrity hash.")
      elif origf.valid:
        print("File is valid")
      else:
        print("File is not valid; bad checksum or bad content for specified file type"); prgerr=bool(args.extract)

    doExtract = False
    if args.extract:
      try: os.stat(args.output)
      except: mkfolders(args.output); doExtract=True
      else:
        try: os.stat(args.output+"/")
        except: print("Cannot extract; destination must be a folder, not a file."); prgerr=True
        else: doExtract=True
      
    if doExtract:
      origf.extract(args.output.rstrip("\\/"),args.input, args.bulk)
    
    if args.compress or args.decompress:
    	if args.compress: origf.head.compress = True
    	if args.decompress: origf.head.compress = False
    	flushFile = True
    
    if args.setname != None:
    	origf.head.creatorName = args.setname
    	origf.head.uploaderName = args.setname
    	origf.head.creatorID = 0
    	origf.head.uploaderID = 0
    	flushFile = True
    
    if flushFile or args.update:
    	origf.updateCmnHdr()
    	d = origf.pack()
    	with open(args.input,"wb") as f:
    		f.truncate()
    		f.write(d)
    		f.flush()

else:
#except:
  errtype, errvalue, errtrace = sys.exc_info()
  if errtype==KeyboardInterrupt:
    print("Script was stopped."); prgerr=0xc0ffee
  elif errtype!=SystemExit:
    #print("\n An error has occured while running the script.\n")
    #traceback.print_exception(errtype, errvalue, errtrace)
    print("\n An exception occured (%s):\n  %s\n" % (str(errtype).split("'")[1],str(errvalue)))
    prgerr=True

exit(prgerr)