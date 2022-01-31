#!/usr/bin/python3

if 0:
	from PTCFile.SBFile.CommonHeader import obj as CmnHdr
	from PTCFile.SBFile.TextFile import TextFile
	from PTCFile.SBFile.DataFile import DataFile
	from PTCFile.SBFile.MetaFile import MetaFile
	from PTCFile.SBFile.ProjectFile import PRJFile

def FileFormatValid(f):
	h:CmnHdr = f.head
	fmtn = h.getFTypeStr()
	d:bytearray = f.data
	if h.isForSwitch():
		pass
	else:
		if fmtn == "TXT":
			try: d.decode("utf-8")
			except: return True
	return False

def setupFormatClass(f):
	h:CmnHdr = f.head
	fmtn = h.getFTypeStr()
	if h.isForSwitch():
		if fmtn == "TXT": f.fmt = TextFile()
	else:
		pass