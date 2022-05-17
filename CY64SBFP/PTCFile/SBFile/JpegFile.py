#!/usr/bin/python3

import PTCFile.ImgCnv as imgsvc

class JpegFileData:
  image = b''
  def __init__(s, b):
    s.image = b
  def pack(s):
    return s.image

class JpegFile:
  def __init__(s, sbf):
    sbf.neck = None
    sbf.data = JpegFileData(sbf.data)
  def extract(s, f, sbf):
    d=open(f+"/%s.jpg"%(sbf.name),'w')
    d.write(sbf.data.data)
    d.close()