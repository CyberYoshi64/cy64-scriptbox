#!/usr/bin/python3

from PTCFile.SBFile.CommonHeader import CmnHdr
from PTCFile.SBFile.TextFile import TextFile
from PTCFile.SBFile.DataFile import DataFile
from PTCFile.SBFile.GRPFile import GRPFile
from PTCFile.SBFile.MetaFile import MetaFile
from PTCFile.SBFile.ProjectFile import ProjectFile
import PTCFile.CY64Ware as CYW

def setFileClass(s)->None:
    if hasattr(s,"head") and hasattr(s,"fmt") and \
    hasattr(s,"neck") and hasattr(s,"data"):
        try:
            if CYW.CYW4PTC_ENABLE and hasattr(CYW,"CYW4PTC_KnownFmt"):
                    for i in CYW.CYW4PTC_KnownFmt:
                        name0,name1 = 0,0
                        for j in i.PREFPREFIX: name0 |= s.name.startswith(j)
                        for j in i.PREFSUFFIX: name1 |= s.name.endswith(j)
                        if (name0 and name1) or i.guessFormat(s):
                            s.fmt = i(s)
                            return
        except Exception as e: raise Exception(e)
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