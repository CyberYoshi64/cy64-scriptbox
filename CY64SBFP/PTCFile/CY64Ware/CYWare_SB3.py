#!/usr/bin/python3

import math, struct
import PTCFile.ImgCnv as cv
from PTCFile.SBFile import DataFile, GRPFile, TextFile

# .###### ##    ## ##    ##     .##  ###### ######  .######.
# ##      ##    ## ## .. ##   .#### ##      ##   ##       ##
# ##      `######´ ##.##.## .##´ ##  #####  ######   -#####
# ##         ##    ###´`### #######      ## ##   ##       ##
# `######    ##    ##´  `##      ## ######  ######  `######´
#
#                 CY64Ware For SmileBASIC3
#                  2019-2022 CyberYoshi64

### CFD (Compressed Font Data)
## Rudimentary format — Maintained as legacy
# WARNING:
# - No data verification (no integrity checks)
# - Can't hold additional information
## Prefered base file type: DAT
## Format:
# [Struct] Length: 0x84 ; Count: 1-*
# - 0x00-0x03 - Int32 - Character ID
# - 0x04-0x83 - Uint16[64] - Graphic data for character
# (Reference: FONTDEF in SmileBASIC Help)

class CYW4SB3_CFD_Data:
  definitions = []
  def __init__(s,fco) -> None:
    s.definitions = []
    idx=28 # Skipping secondary data header
    try:
      while idx < len(fco):
        char = struct.unpack("<I",fco[idx:idx+4])[0]
        cdat = b''
        for i in range(4,132,4):
          cdat += fco[idx+i+2:idx+i+4]+fco[idx+i:idx+i+2] # Why did I try compensating endianness? This is why I shouldn't have…
        idx += 132
        s.definitions.append((char, cdat))
    except: pass
  def pack(s)->bytes:
    h=DataFile.mkPCBN(dim=[33*len(s.definitions)])
    d=b''
    for i in s.definitions:
      d += int.to_bytes(i[0],4,"little")+i[1]
    return h+d
class CYW4SB3_CFD:
  CTYPENAME = "CYW-CFD"
  PREFPREFIX = ["B"]
  PREFSUFFIX = [".CFD"]
  def guessFormat(sbf)->bool: return False # too generic format, literally anything could be valid here
  def __init__(s,sbf)->None:
    sbf.data = CYW4SB3_CFD_Data(sbf.data)
    sbf.neck = None
  def extract(s,f,sbf):
    d=open(f+"/desc.rsf",'a')
    d.write("""\
Property:
    ContentType: "%s"
""" % s.CTYPENAME)
    d.close()
    ob=b''; d=open(f+"/font.csv","wb"); d.truncate(0)
    for i in sbf.data.definitions:
      ob += i[1]; d.write((str(i[0])+",").encode("utf8"))
    w=192; h=math.ceil(len(sbf.data.definitions)/(w/8))*8
    a = []
    for i in range(h):
      b = []
      for j in range(w): b.append(0)
      a.append(b)
    for i in range(len(ob)//2):
      x=int(i//64*8 + (i%8))
      y=int(x//w*8 + int(i/8)%8)
      a[y][x%w] = int.from_bytes(ob[i*2:i*2+2],"little")
    cv.saveImageToFile(cv.simparr2buf([cv.CNV_RGBA5551, a]), "%s/font.png"%f)
    d.close()