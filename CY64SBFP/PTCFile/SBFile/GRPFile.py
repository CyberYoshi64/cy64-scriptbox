#!/usr/bin/python3

try: import PTCFile.CY64Ware as CYW
except: pass

import PTCFile.ImgCnv as imgsvc
import PTCFile.SBFile.DataFile as DataFile
import struct, os

DATATYPE_GRPFMT = (None, None, None, imgsvc.CNV_RGBA5551, imgsvc.CNV_ARGB8, None)

class GRPFileData:
  MAGIC=b'PCBN000'; formatVer = 5
  type = 4; dim = [0, 0, 0, 0]; dimc = 1
  imageData = [None, 0, 0, b'']

  def __init__(s, d):
    if d!=None:
      mgc, s.formatVer, s.type, dimc, dim0, dim1, dim2, dim3 = \
      struct.unpack("<7ssHHiiii", d[:28])
      if mgc!=s.MAGIC: return
      if dimc != 2: return
      try: (b"1",b"5").index(s.formatVer)
      except: return
      s.dimc = dimc
      s.dim = [dim0, dim1, dim2, dim3]
      try:
        s.imageData = [DATATYPE_GRPFMT[s.type],dim0,dim1,bytearray(d[28:])]
        if s.imageData[0]==None: return
      except: return
  def pack(s):
    return struct.pack(
      "<7ssHHiiii", s.MAGIC, s.formatVer, s.type, 2, s.dim[0], s.dim[1], s.dim[2], s.dim[3]
    ) + s.imageData[3]

class GRPFile:
  def __init__(s, sbf):
    sbf.neck = None
    sbf.data = GRPFileData(bytes(sbf.data))
    pass
  def extract(s, f, sbf):
    d=open(f+"/desc.rsf",'a')
    d.write("""\
Property:
    ContentType: "GRP"
    DataType:    %d
    Filtering:   "None"
""" % (sbf.data.type))
    d.close()
    imgsvc.saveImageToFile(sbf.data.imageData,"%s/%s.png"%(f,sbf.name))