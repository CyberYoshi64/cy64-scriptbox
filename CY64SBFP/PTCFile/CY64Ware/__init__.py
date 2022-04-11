#!/usr/bin/python3

import PTCFile.ImgCnv as cv
import struct

## CY64Ware for SmileBASIC
## 2021-2022 CyberYoshi64
## 
## This module is for extensions to SmileBASIC.
## If you only want vanilla SmileBASIC types,
## please avoid this module and associated elements.

# Kill switch
CYW4PTC_ENABLE = True

#----------------------------------------------------
# File Formats

### CYW4SB3 CFD (Compressed Font Data)
## Rudimentary format — Maintained as legacy
# WARNING:
# - No failsafes / verification
# - Can't hold additional information
## Prefered base file type: DAT
## Format:
# [Struct] Length: 0x84 ; Count: 0-*
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
    h=b'PCBN0001\x04\0\x01\0'+int.to_bytes(1+33*len(s.definitions),4,"little")+b'\0'*12 # Crafted header - sufficient for this format
    d=b''
    for i in s.definitions:
      d += int.to_bytes(i[0],4,"little")+i[1]
    return h+d
class CYW4SB3_CFD:
  ctypeName = "CYW-CFD"
  def preferedPrefix()->str: return "B"
  def preferedExtension()->str: return ".CFD"
  def guessFormat(sbf)->bool: return False # too generic format, literally anything could be valid here
  def __init__(s,sbf)->None:
    sbf.data = CYW4SB3_CFD_Data(sbf.data)
    sbf.neck = None
  def extract(s,f,sbf):
    d=open(f+"/desc.rsf",'a')
    d.write("""\
Property:
    ContentType: "%s"
""" % s.ctypeName)
    d.close()
    ob=b''; d=open(f+"/font.csv","wb"); d.truncate(0)
    for i in sbf.data.definitions:
      ob += i[1]; d.write((str(i[0])+",").encode("utf8"))
    cv.saveImageToFile([cv.CNV_RGBA5551, 8, len(sbf.data.definitions)*8, bytearray(ob)], "%s/font.png"%f)
    d.close()

#----------------------------------------------------
# Misc

CYW4PTC_KnownFmt = [
  CYW4SB3_CFD #,\ # (SB3) Compressed Font Data
  # CYW4SB3_PCM16 #,\ # (SB3) 16bit PCM sample
]