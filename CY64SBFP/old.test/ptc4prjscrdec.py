#!/usr/bin/python3

import PTCFile.ImgCnv as PTCimcv
from PTCFile.Helper import *
from sys import argv
import os, glob

fol=argv[1].rstrip("\\/")+"/"

try: os.stat(fol)
except: raise FileNotFoundError(fol+" is not a valid folder")

files = glob.glob(fol+"*")
print(fol, files)
# buf=PTCimcv.getImageFromFile()