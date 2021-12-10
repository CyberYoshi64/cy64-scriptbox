#!/usr/bin/python3

import glob
import os
if (len(os.sys.argv) != 3):
	print("Usage: {} <folder> <outname>".format(os.sys.argv[0]))
	print("  folder : Relative path to folder containing bcwavs")
	print("  outname: File name to output CYCWAR to (w/o extension)")
	exit(1)

# Header (0x10 bytes long)
# 0x0-0x7 - Header magic (CY64CWAR)
# 0x8-0x9 - File version (v3)
# 0xa-0xb - Number of BCWAVs in file (will change automatically)
# 0xc-0xf - Absolute offset to BCWAV data (depends on # of files)

# File portions
header=b''
hdrmgc=b'CY64CWAR'+int.to_bytes(3,2,"little")
fltbl=b''

# Misc
flist=glob.glob("."+os.sep+os.sys.argv[1]+os.sep+"*.bcwav")
fname=os.sys.argv[2]+".cycwar"
dng=0

# Open output file
csar = open(fname,'wb+')

# Loop through each bcwav file in assets/snd, add their names and file sizes to the header and copy contents to fltbl
for i in flist:
	cwav=open(i,"rb")
	cwavsz=os.stat(i).st_size
	flgs=0
	j=i[13:len(i)-6]
	if j.endswith("_2ch"):
		j=j[0:len(j)-4]
		flgs |= 1
	if j[len(j)-2]=="_":
		num=ord(j[len(j)-1])-47
		if num>1 and num<10:
			j=j[0:len(j)-2]
			flgs |= num*2
	else:
		flgs |= 2
	if len(j)<64:
		header+=(str.encode(j))+b'\0'+int.to_bytes(cwavsz,4,"little")+int.to_bytes(flgs,1,"big")
		fltbl += cwav.read(cwavsz)
	else:
		dng += 1
	cwav.close()

header=hdrmgc+int.to_bytes(len(flist),2,"little")+int.to_bytes(len(header)+16,4,"little")+header

# Write the components, close the file and exit
csar.write(header)
csar.write(fltbl)
csar.close()

if dng:
	print("Built \""+fname+"\" with "+str(dng)+" error"+"s"*(i!=1)+".")
	print("You may use this file, however, your program may behave unexpectedly.")

else:
	print("Built \""+fname+"\" with no errors.")

exit(0)
