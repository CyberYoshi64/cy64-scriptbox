#!/usr/bin/python3

from PTCFile.SBFile.CommonHeader import CmnHdr
from PTCFile.SBFile.TextFile import TextFile
from PTCFile.SBFile.DataFile import DataFile
from PTCFile.SBFile.GRPFile import GRPFile
from PTCFile.SBFile.MetaFile import MetaFile
from PTCFile.SBFile.ProjectFile import ProjectFile

def setFileClass(s):
    if hasattr(s,"head") and hasattr(s,"fmt") and\
    hasattr(s,"neck") and hasattr(s,"data"):
        ftyp = s.head.getFTypeStr()
        if ftyp=="TXT":
            s.fmt = TextFile(s)
        if ftyp=="DAT":
            if not s.head.isForSwitch() and s.head.getFIconStr()=="GRP":
                s.fmt = GRPFile(s)
            else:
                s.fmt = DataFile(s)
        if ftyp=="GRP":
            s.fmt = GRPFile(s)
        if ftyp=="META":
            s.fmt = MetaFile(s)
        if ftyp=="PRJ":
            s.fmt = ProjectFile(s)
    pass