#!/usr/bin/python3

import struct
import PTCFile.ImgCnv as imcv

class MetaData:
    MAGIC = b'PCPM0005'
    name = "New project"
    desc = "This is a new project."
    icon = [imcv.CNV_ARGB8, 0, 0, b'']
    size = 0x2B20
    def __init__(s, sd):
        if type(sd)!=bytes:
            sd = sd.raw
            if type(sd)!=bytes: return
        if len(sd)<4636: return
        mgc, s.name, s.desc, icsz = struct.unpack("<8s48s4576si",sd[:4636])
        if mgc != s.MAGIC: return
        s.name = str(s.name, "utf-16-le","ignore")
        s.desc = str(s.desc, "utf-16-le","ignore")
        s.icon[1] = s.icon[2] = icsz
        s.icon[3] = sd[4636:4636+pow(icsz,2)*4]
    def pack(s):
        if s.icon[1]!=s.icon[2]: return None
        return struct.pack("<8s48s4576si",
            s.MAGIC, bytes(s.name,"utf-16-le","ignore"),
            bytes(s.desc,"utf-16-le","ignore"), s.icon[1]
        ) + s.icon[3] + b'\0\0\0\0'

class MetaNeck:
    usesHash=False

class MetaFile:
    def __init__(s, sbf):
        sbf.data = MetaData(sbf.data)
        pass