#!/usr/bin/python3

import PTCFile.PRJMake as prjm
from PTCFile.SBFile.CommonHeader import CmnHdr
import PTCFile.SBFile.Parser as Parser
from PTCFile.Helper import mkfolders
import hashlib, zlib, hmac, io

HMAC_KEY = b'nqmby+e9S?{%U*-V]51n%^xZMk8>b{?x]&?(NmmV[,g85:%6Sqd"\'U")/8u77UL2'

def newSBFile(data):
  s = SBFile(); fsz = 0
  fsz = s.head.loadFromBuf(data)
  if fsz: return
  if s.usesHash(): s.data = data[fsz:-20]
  else: s.data = data[fsz:]
  if s.head.compress: s.data=zlib.decompress(s.data)
  Parser.setFileClass(s)
  if type(s.data)==bytes: s.data=bytearray(s.data)
  if s.usesHash(): s.valid = (data[-20:] == hmac.new(HMAC_KEY, data[:-20], hashlib.sha1).digest()) or not s.usesHash()
  return s

def newSBFileHeadless(data):
  s = SBFile(); s.data = data
  s.updateCmnHdr()
  Parser.setFileClass(s)
  if type(s.data)==bytes: s.data=bytearray(s.data)
  return s

class SBFile:
  FORMAT_TYPE = 1
  name = "NEWFILE"# File name (obtained from file descriptor on-load)
  head = CmnHdr() # Blank header
  fmt  = None     # Subclass dealing with neck/data
  neck = None     # Subsidiary header
  data = False    # Main data
  valid = False   # Is file valid on-load?
  def usesHash(s)->bool:
    # No idea why META is the only format without footer
    # Likely only intended to be in the Project file type
    # as it has an additional Meta and it does have a footer.
    return s.head.getFileTypeName()!="META" 
  def makeHash(s)->bytes:
    if not s.usesHash(): return b''
    return s.pack()[-20:]
  def getDataSize(s)->int:
    rawDat = b''
    if hasattr(s.data, "pack"): rawDat = s.data.pack()
    elif type(s.data) == bytes: rawDat = s.data
    elif type(s.data) == bytearray: rawDat = s.data
    if s.head.compress: rawDat = zlib.compress(rawDat)
    return len(rawDat)
  def updateCmnHdr(s)->None:
    rawDat = b''
    if hasattr(s.data, "pack"): rawDat = s.data.pack()
    elif type(s.data) == bytes: rawDat = s.data
    if s.head.compress: rawDat = zlib.compress(rawDat)
    s.head.dataSize = len(rawDat)
    s.head.updateModDate()
  def pack(s)->bytes:
    b=b''; d=b''; h=b''
    if hasattr(s.head, "pack"): b += s.head.pack()
    if hasattr(s.neck, "pack"): d += s.neck.pack()
    if hasattr(s.data, "pack"): d += s.data.pack()
    elif type(s.data) == bytes: d += s.data
    elif type(s.data) == bytearray: d += bytes(s.data)
    if s.head.compress: d = zlib.compress(d)
    if s.usesHash(): h=hmac.new(HMAC_KEY, b+d, hashlib.sha1).digest()
    return b+d+h
  def __init__(s, fd=None) -> int:
    s.valid = False; fsz=0
    if type(fd)==io.BufferedReader:
      s.name = fd.name.split("\\")[-1].split("/")[-1]
      fd.seek(0,2); fsz=fd.tell(); fd.seek(0,0)
      if fsz<100:
        raise Exception("File is truncated. Not enough bytes.")
      d=fd.read(fsz-20); f=fd.read(20)
      s.valid = (f == hmac.new(HMAC_KEY, d, hashlib.sha1).digest())
      fd.seek(0,0)
      if s.head.loadFromFD(fd)<0:
        raise Exception("File is truncated. Not enough bytes.")
      fsz -= fd.tell() + 20 * s.usesHash()
      s.data = fd.read(fsz)
      if s.head.compress: s.data=zlib.decompress(s.data)
      Parser.setFileClass(s)
      if type(s.data)==bytes: s.data=bytearray(s.data)
  def extract(s,f,onm,verb=False):
    prjname = onm.split("/")[-1]
    FCATDIR=f+"/%s"%prjname
    mkfolders(FCATDIR)
    if not verb:
      print("Outputting in %s ..."%f)
      print("Extracting file head...")
    s.head.extract(FCATDIR, s.name)
    if hasattr(s.fmt,"extract"):
      if not verb: print("Extracting file contents...")
      s.fmt.extract(FCATDIR, s)
    pass
