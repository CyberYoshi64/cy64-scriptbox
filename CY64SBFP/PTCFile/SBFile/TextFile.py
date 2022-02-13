#!/usr/bin/python3

class TextFileData:
  string = ""
  lineCount,wordCount = 0,0
  def __init__(s, tco):
    s.string = tco
    s.lineCount = s.string.count("\n")
    s.wordCount = s.string.split()
  def pack(s):
    return bytes(s.string,"utf8")

class TextFile:
  def __init__(s, sbf):
    sbf.neck = None
    sbf.data = TextFileData(sbf.data.decode("utf8","ignore"))
  def extract(s, f, sbf):
    d=open(f+"/%s.txt"%(sbf.name),'w')
    d.write(sbf.data.string)
    d.close()
