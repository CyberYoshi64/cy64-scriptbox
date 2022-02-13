#!/usr/bin/python3
import datetime, struct
class CmnHdr:
  srcConsole, fileType, compress, fileIcon, dataSize, modYear,\
  modMonth, modDay, modHour, modMinute, modSecond, modWeekDay =\
  (0,0,0,0,0,0,0,0,0,0,0,0)
  creatorName, creatorID, uploaderName, uploaderID =\
  ("CY64-PTC-FM",0xC0FFEE,"CY64-PTC-FM",0xC0FFEE)
  creator_uploadID, uploader_uploadID = (0,0)

  HEADER_SHARED_LEN = 28
  SB3_HDRSIZE, SB4_HDRSIZE = (0x50,0x70)
  SB3_USRLEN, SB4_USRLEN = (18,32)
  
  def extract(s,f,n):
    d=open(f+"/desc.rsf",'w')
    d.write("""\
#CYWPTCPRJDSC 1

File:
    Type:      "%s"
    Name:      "%s"
    Compress:  %s
    Creator:   "%s"
    CreatorID: "%08x"
    Editor:    "%s"
    EditorID:  "%08x"
    UploadID1: "%016x"
    UploadID2: "%016x"

Note:
    FileSize:   %d
    EditDate:   "%d,%04d/%02d/%02d,%02d:%02d:%02d"
    FileIcon:   "%d"

""" % (s.getFTypeStr(), n, ("False","True")[bool(s.compress)], \
       s.creatorName, s.creatorID, \
       s.uploaderName, s.uploaderID, \
       s.creator_uploadID, s.uploader_uploadID, s.dataSize, s.modWeekDay, \
       s.modYear, s.modMonth, s.modDay, s.modHour, s.modMinute, s.modSecond,\
       s.fileIcon
      ))
    d.close()

  def isForSwitch(s)->int:
    try: return bool(int(s.srcConsole / 4))
    except: return -1

  def updateModDate(s) -> None:
    t=datetime.datetime.now()
    s.modYear, s.modMonth, s.modDay, s.modHour, s.modMinute, s.modSecond =\
    t.year, t.month, t.day, t.hour, t.minute, t.second
    s.modWeekDay = t.weekday()

  def getUsernameEncoding(s): return ("iso8859_15","utf-8")[s.isForSwitch()]
  def getValidHeaderSize(s): return (0x50,0x70)[s.isForSwitch()]
  def getUsernameLen(s): return (18,32)[s.isForSwitch()]
  def getWeekdayStr(s)->str:
    try: return ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")[s.modWeekDay]
    except: return "(Bad weekday)"
  def getFTypeStr(s)->str:
    if s.isForSwitch():
      try: return ("TXT","DAT","GRP","PRJ","META")[s.fileType]
      except: return "UNK"
    else:
      try: return ("TXT","DAT","PRJ")[s.fileType]
      except: return "UNK"

  def getFIconStr(s)->str:
    if s.isForSwitch(): return ""
    elif s.fileType == 0:
      try: return ("TXT","PRG","GRP")[s.fileIcon]
      except: return "UNK"
    elif s.fileType == 1:
      try: return ("DAT","PRG","GRP")[s.fileIcon]
      except: return "UNK"
    return ""
  
  def getFileTypeName(s)->str:
    name=s.getFTypeStr()
    if s.isForSwitch(): return name
    ict=s.getFIconStr()
    if len(ict): name += "/" + ict
    return name

  def pack(s) -> bytes:
    headerSize = s.getValidHeaderSize()
    usernameSize = s.getUsernameLen()
    padding = headerSize - s.HEADER_SHARED_LEN - usernameSize * 2
    return struct.pack(
      "<HHHHIHBBBBBB {0}s{0}sII QQ{1}".format(usernameSize, ("","4x")[s.isForSwitch()]),
      s.srcConsole, s.fileType, s.compress,\
      s.fileIcon, s.dataSize,\
      s.modYear, s.modMonth, s.modDay, s.modHour,\
      s.modMinute, s.modSecond, s.modWeekDay, \
      s.creatorName.encode(s.getUsernameEncoding(),"ignore"), \
      s.uploaderName.encode(s.getUsernameEncoding(),"ignore"), \
      s.creatorID, s.uploaderID, s.creator_uploadID, s.uploader_uploadID
    )

  def loadFromFD(s, fd)->int:
    isSwitch=False; b=fd.read(s.SB3_HDRSIZE)
    if len(b)<s.SB3_HDRSIZE: return 0
    s.srcConsole = struct.unpack("<H",b[:2])[0]
    if s.isForSwitch(): isSwitch=True
    if isSwitch:
      fd.seek(-s.SB3_HDRSIZE, 1)
      b = fd.read(s.SB4_HDRSIZE)
      if len(b)<s.SB4_HDRSIZE: return 0
    return s.continueLoad(b)
    
  def loadFromBuf(s, buf)->int:
    isSwitch=False; b=buf[:s.SB3_HDRSIZE]
    if len(b)<s.SB3_HDRSIZE: return 0
    s.srcConsole = struct.unpack("<H",b[:2])[0]
    if s.isForSwitch(): isSwitch=True
    if isSwitch:
      b = buf[:s.SB4_HDRSIZE]
      if len(b)<s.SB4_HDRSIZE: return 0
    return s.continueLoad(b) * len(b)
    
  def continueLoad(s, b):
    isSwitch = s.isForSwitch()
    s.srcConsole, s.fileType, s.compress,\
    s.fileIcon, s.dataSize,\
    s.modYear, s.modMonth, s.modDay, s.modHour,\
    s.modMinute, s.modSecond, s.modWeekDay =\
    struct.unpack("<HHHHIHBBBBBB",b[:20])
    usrnmsz=(s.SB3_USRLEN, s.SB4_USRLEN)[isSwitch]
    padstart = 44+usrnmsz*2
    cusn, uusn, s.creatorID, s.uploaderID, \
    s.creator_uploadID, s.uploader_uploadID =\
    struct.unpack("<{0}s{0}sIIQQ".format(usrnmsz),b[20:padstart])
    s.creatorName=cusn.decode(s.getUsernameEncoding(),"ignore").split("\0")[0]
    s.uploaderName=uusn.decode(s.getUsernameEncoding(),"ignore").split("\0")[0]
    return 1