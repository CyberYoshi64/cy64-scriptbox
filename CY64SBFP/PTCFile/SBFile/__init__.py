#!/usr/bin/python3

from PTCFile.SBFile.CommonHeader import obj as CommonHeader
import PTCFile.SBFile.Parser as Parser
import hashlib, zlib, hmac, io

HMAC_KEY = b'''nqmby+e9S?{%U*-V]51n%^xZMk8>b{?x]&?(NmmV[,g85:%6Sqd"'U")/8u77UL2'''

class SBFile:
    FORMAT_TYPE = 1
    head = CommonHeader()	# Blank header
    fmt  = None
    neck = None				# Subsidiary header
    data = False			# Main data
    foot = b''				# HMAC-SHA1 hash used for verification
    valid = True
    def usesHash(s)->bool:
        if s.head.getFileTypeName()=="META": return
        return True
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
        if hasattr(s.data, "pack"): d += s.data.pack()
        elif type(s.data) == bytes: d += s.data
        elif type(s.data) == bytearray: d += bytes(s.data)
        if s.head.compress: d = zlib.compress(d)
        if s.usesHash(): h=hmac.new(HMAC_KEY, b+d, hashlib.sha1).digest()
        return b+d+h
    def __init__(s, fd=None, vf=True) -> int:
        s.foot = b''; s.valid = False
        s.error=0; s.errorstr=""; fsz=0
        if type(fd)==io.BufferedReader:
            if vf: fd.seek(0,2); fsz=fd.tell(); fd.seek(0,0)
            if s.head.loadFromFD(fd):
                s.error = 1
                s.errorstr = "File is truncated. Not enough bytes."
                return
            if not vf: fsz=s.head.dataSize
            else: fsz -= fd.tell() + 20 * s.usesHash()
            s.data = fd.read(fsz)
            if s.head.compress: s.data=zlib.decompress(s.data)
            s.data=bytearray(s.data)
            if s.usesHash(): s.foot = fd.read(20)
            if Parser.FileFormatValid(s) != False:
                s.error = 2
                s.errorstr = "File content is not valid for its configured type."
            s.valid = (s.foot == s.makeHash()) or not s.usesHash()
