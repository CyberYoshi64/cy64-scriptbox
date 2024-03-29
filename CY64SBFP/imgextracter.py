#!/usr/bin/python3
import PTCFile, struct
from sys import argv

if len(argv)<3: print("Usage: %s [file] [mode 0/1-to/fromGRP]"%argv[0]); exit(0)
inf=argv[1]
outf="BOUT2.GRP"
outi="in.png"
outf2="out3.png"

if not int(argv[2]):
	f=open(inf,"rb")
	origfobj = PTCFile.File(f)
	f.close()
	origf = origfobj.format
	#imgb = origfobj.format.data.imageData
	print("Get Image from File")
	imgb = PTCFile.ImgCnv.getImageFromFile(outi)
	w, h = imgb[1:3]
	print("Convert to RGBA5551")
	imgb = PTCFile.ImgCnv.convertImage(imgb, PTCFile.ImgCnv.CNV_RGBA5551, 0)
	origf.data = b'PCBN0001'+struct.pack("<HHIIII",3,2,w,h,0,0)+imgb[3]
	origf.head.compress = True
	f=open(outf+"@C","wb")
	f.truncate(0)
	f.write(origf.pack())
	f.flush(); f.close()
	origf.head.compress = False
	f=open(outf,"wb")
	f.truncate(0)
	f.write(origf.pack())
	f.flush(); f.close()
else:
	f=open(inf,"rb")
	w,h=512,512
	f.seek(0x6C)
	print("Get image back from written file")
	img = bytearray(f.read(w*h*2))
	f.close()
	print("Convert to ARGB8")
	buf = PTCFile.ImgCnv.convertImage([PTCFile.ImgCnv.CNV_RGBA5551, w, h, img], PTCFile.ImgCnv.CNV_BGRA8, 0)
	print("Saving file")
	print(PTCFile.ImgCnv.saveImageToFile(buf, outf2))
	
