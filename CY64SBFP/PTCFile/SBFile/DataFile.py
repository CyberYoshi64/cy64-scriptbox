#!/usr/bin/python3

try: import PTCFile.CY64Ware as CYW
except: pass

import struct, os

DATATYPE_STCTFMT = ("b","B","h","H","i","d") # S8,U8,S16,U16,U32,dbl

class DataFileContent:
  MAGIC=b'PCBN000'; formatVer = 5
  type = 4; dim = [0, 0, 0, 0]; dimc = 1
  data = b''

  def __init__(s, d):
    if d!=None:
      mgc, s.formatVer, s.type, dimc, dim0, dim1, dim2, dim3 = \
      struct.unpack("<7ssHHiiii", d[:28])
      if mgc!=s.MAGIC: return
      if dimc<1 or dimc>4: return
      try: (b"1",b"5").index(s.formatVer)
      except: return
      s.dimc = dimc
      s.data = d[28:]
      s.dim = [dim0, dim1, dim2, dim3]
      try:
        tl=struct.calcsize(DATATYPE_STCTFMT[s.type]); dl=1
        for i in range(dimc):
          dl *= s.dim[i]
        if dl*tl != len(s.data): raise ValueError("Data length mismatch!")
      except: pass
  def extract(s,f): pass
  def pack(s):
    return struct.pack(
      "<7ssHHiiii", s.MAGIC, s.formatVer, s.type, s.dimc, s.dim[0], s.dim[1], s.dim[2], s.dim[3]
    ) + s.data


class DataFile:
  def __init__(s, sbf):
    sbf.neck = None
    sbf.data = DataFileContent(bytes(sbf.data))
  def extract(s, f, sbf):
    d=open(f+"/desc.rsf",'a')
    d.write("""\
Property:
    ContentType: "DAT"
    DataType:    %d
""" % (sbf.data.type))
    d.close()
    a=[]; desz=struct.calcsize(DATATYPE_STCTFMT[sbf.data.type])
    try:
      for i in range(0, len(sbf.data.data), desz):
        a.append(struct.unpack("<%s"%DATATYPE_STCTFMT[sbf.data.type],\
        sbf.data.data[i:i+desz])[0])
    except: pass
    d=open(f+"/%s.csv"%(sbf.name),'wb')
    d.write(b"%d,%d,%d,%d,%d\n\n" % (
      sbf.data.dimc, sbf.data.dim[0],sbf.data.dim[1],\
      sbf.data.dim[2], sbf.data.dim[3]
    ))
    b=sbf.data.dimc == 2; c=sbf.data.dim[0]
    for i in range(len(a)):
      if b and (i % c)==(c-1): d.write(b"%d\n"%a[i])
      else: d.write(b"%d,"%a[i])
    d.close()