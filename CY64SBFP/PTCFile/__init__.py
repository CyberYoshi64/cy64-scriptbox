#!/usr/bin/python3
import io

from PTCFile.SBFile import SBFile
import PTCFile.ImgCnv as ImgCnv

class File:
	errorstr = ""; error=0
	format = None
	def __init__(self, fd=None, vf=True) -> None:
		if type(fd)==io.BufferedReader:
			startOff=fd.tell()
			b=fd.read(9)
			b=b[:5]+b[6:]
			if b==b"PETC000R":
				raise TypeError("Files for Petitcom and mkII are not supported.")
			fd.seek(startOff, 0)
		self.format=SBFile(fd,vf)
	def extract(s, e):
		if type(e)!=tuple and type(e)!=list: return 1
		try: e.index("all")
		except: pass
		else: e=("head:all","subhdr:all","data:all")
		i:str=0
		for i in e:
			if type(i)!=str: return 1
			if len(i.split(":")) != 2: return 1
			et = i.split(":")
			try: ("all","head","subhdr","data","x").index(et[0])
			except: return 2
			if et[0]=="x":
				pass
			elif et[0]=="head":
				if hasattr(s.format.head,"extract"): s.format.head.extract(et[1])
			elif et[0]=="subhdr":
				if hasattr(s.format,"neck"):
					if hasattr(s.format.neck,"extract"): s.format.neck.extract(et[1])
			elif et[0]=="data":
				if hasattr(s.format.data,"extract"): s.format.data.extract(et[1])
			return 0
