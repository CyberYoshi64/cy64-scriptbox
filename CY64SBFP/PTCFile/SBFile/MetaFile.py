#!/usr/bin/python3

import struct
import PTCFile.ImgCnv as imcv

class MetaData:
    MAGIC = b'PCPM0005'
    name = "New project"
    desc = "This is a new project."
    size = 0x2B20
    def __init__(s, sd):
        if type(sd)!=bytes:
            sd = sd.raw
            if type(sd)!=bytes: return
        if len(sd)<4636: return
        s.icon = [imcv.CNV_ARGB8, 0, 0, b'']
        try: mgc, s.name, s.desc, icsz = struct.unpack("<8s48s4576sI",sd[:4636])
        except: return
        if mgc != s.MAGIC: return
        s.name = str(s.name, "utf-16-le","ignore").split("\0")[0]
        s.desc = str(s.desc, "utf-16-le","ignore").split("\0")[0]
        s.icon[1] = s.icon[2] = icsz
        s.icon[3] = bytearray(sd[4636:-4])
        print(len(s.icon[3]))
    def pack(s):
        return struct.pack("<8s48s4576sI",
            s.MAGIC, bytes(s.name,"utf-16-le","ignore"),
            bytes(s.desc,"utf-16-le","ignore"), s.icon[1]
        ) + s.icon[3] + b'\0'*4

class MetaNeck:
    usesHash=False

class MetaFile:
    def __init__(s, sbf):
        sbf.neck = MetaNeck()
        sbf.data = MetaData(sbf.data)
    def extract(s, f, sbf):
        print(imcv.saveImageToFile(sbf.data.icon,"%s/icon.png"%f))
        d=open(f+"/desc.rsf","a")
        d.write("""ProjectMeta:
    Title: "%s"
    Description:
    \"\"\"
%s
    \"\"\"
""" % (sbf.data.name, sbf.data.desc.strip()))
        d.close()