#!/usr/bin/python3
import PTCFile, struct

outf="BOUT2.GRP"
outi="out2.png"
outf2="out3.png"

f=open("cbin/BBG_DESK00.GRP","rb")
origfobj = PTCFile.File(f)
f.close()
origf = origfobj.format
imgb = PTCFile.ImgCnv.getImageFromFile(outi)
w, h = imgb[1:3]
imgb = PTCFile.ImgCnv.convertImage(imgb, PTCFile.ImgCnv.CNV_RGBA5551)
origf.data = b'PCBN0001'+struct.pack("<HHIIII",3,2,w,h,0,0)+imgb[3]
f=open(outf,"wb")
f.truncate(0)
f.write(origf.pack())
f.flush(); f.close()

f=open(outf,"rb")
f.seek(0x6C)
img = bytearray(f.read(w*h*2))
f.close()
buf = PTCFile.ImgCnv.convertImage([2, w, h, img], 0, 0)
print(PTCFile.ImgCnv.saveImageToFile(buf, outf2))
