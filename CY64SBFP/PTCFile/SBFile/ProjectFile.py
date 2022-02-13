#!/usr/bin/python3

import struct

import PTCFile.SBFile.MetaFile as Meta

class ProjectArchive:
  files = []
  raw=b''
  def __init__(s, sd):
    s.raw = sd
  def getFiles(s): pass
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
    s.data = sbf.data; flist = []; dataoff = 0
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
    for i in range(s.fileCount):
      d += struct.pack("<I%ss"%((16,36)[bool(s.isSw)]),s.data.files[i][1],s.data.files[i][0].encode("iso8859_15","ignore"))
    return d
class ProjectFile:
  def __init__(s, sbf):
    sbf.data = ProjectArchive(bytes(sbf.data))
    sbf.neck = ProjectHeader(sbf)
    sbf.data.getFiles()
    pass