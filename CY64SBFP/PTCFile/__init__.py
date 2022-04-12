#!/usr/bin/python3
import io, os

from PTCFile.SBFile import SBFile
import PTCFile.ImgCnv as ImgCnv
import PTCFile.PRJMake as PRJMake

class File:
    format = None
    def __init__(self, fd=None) -> None:
        if type(fd)==io.BufferedReader:
            startOff=fd.tell()
            b=fd.read(16)
            c=b[:5]+b[6:10]
            if c==b"PETC000R":
                raise TypeError("Files for Petitcom and mkII are not supported.")
            fd.seek(startOff, 0)
        self.format=SBFile(fd)
