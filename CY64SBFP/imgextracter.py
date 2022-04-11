#!/usr/bin/python3
import PTCFile, struct

outf="BOUT2.GRP"
outi="in.png"
outf2="out3.png"

f=open(outf,"rb")
origfobj = PTCFile.File(f)
f.close()
origf = origfobj.format
#imgb = origfobj.format.data.imageData
print("Get Image from File")
imgb = PTCFile.ImgCnv.getImageFromFile(outi)
w, h = imgb[1:3]
print("Convert to RGBA5551")
imgb = PTCFile.ImgCnv.convertImage(imgb, PTCFile.ImgCnv.CNV_RGBA5551, 3)
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

f=open(outf,"rb")
f.seek(0x6C)
print("Get image back from written file")
img = bytearray(f.read(w*h*2))
f.close()
print("Convert to ARGB8")
buf = PTCFile.ImgCnv.convertImage([2, w, h, img], 0, 0)
print("Saving file")
print(PTCFile.ImgCnv.saveImageToFile(buf, outf2))
