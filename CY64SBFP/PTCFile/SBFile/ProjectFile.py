#!/usr/bin/python3

import struct

import PTCFile.SBFile.MetaFile as Meta

class ProjectArchive:
  files = []
  raw=b''
  def __init__(s, sd):
    s.raw = sd
  def getFiles(s):
    idx:int = 0
    for i in s.files:
      i[2] = s.raw[idx:idx+i[1]]
      idx += i[1]
  def pack(s):
    return s.raw

class ProjectMeta:
  fmt = None
  data = None
  def __init__(s, d):
    s.data = d
    s.fmt=Meta.MetaFile(s)

class ProjectHeader:
  meta = None
  fileCount = 0; prjsz = 0
  data = None; isSw = False
  def usesHash(s): return True
  def __init__(s,sbf):
    s.isSw = sbf.head.isForSwitch()
    s.data = sbf.data; dataoff = 0
    if type(sbf.data)!=ProjectArchive: raise ValueError("Data is not a ProjectArchive class")
    chkHdr=Meta.MetaData.MAGIC
    if sbf.data.raw[:len(chkHdr)]==chkHdr:
      s.meta=ProjectMeta(sbf.data.raw)
      dataoff += s.meta.data.size
    s.prjsz, s.fileCount = struct.unpack("<II",sbf.data.raw[dataoff: dataoff+8])
    dataoff += 8; strs = 4 + (16,36)[bool(s.isSw)]
    for i in range(s.fileCount):
      fsize, fname = struct.unpack("<I%ss"%((16,36)[bool(s.isSw)]),sbf.data.raw[dataoff : dataoff+strs])
      fname = str(fname,"iso8859_15","ignore").split("\0")[0]
      sbf.data.files.append([fname,fsize,b''])
      dataoff += strs
    sbf.data.raw = sbf.data.raw[dataoff:]
  def pack(s):
    d = bytearray()
    if s.meta != None: d += s.meta.data.pack()
    d += struct.pack("<II",s.prjsz,s.fileCount)
    for i in s.data.files:
      d += struct.pack("<I%ss"%((16,36)[bool(s.isSw)]),i[1],i[0].encode("iso8859_15","ignore"))
    for i in s.data.files:
      d += i[2]
    return d
class ProjectFile:
  def __init__(s, sbf):
    sbf.data = ProjectArchive(bytes(sbf.data))
    sbf.neck = ProjectHeader(sbf)
    sbf.data.getFiles()
  def extract(s, f, sbf):
    import os
    if sbf.neck.meta != None: sbf.neck.meta.fmt.extract(f, sbf.neck.meta)
    os.makedirs(f+"/raw",exist_ok=True)
    print("File count: {}".format(len(sbf.data.files)))
    for i in sbf.data.files:
      d=open(f+"/raw/%s"%(i[0]),'wb'); d.truncate(0)
      d.write(i[2]); d.flush(); d.close()
