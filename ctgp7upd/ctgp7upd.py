import os, requests, time
from typing import Any
from sys import argv

def mkfolders(fol):
	global mainfolder
	g=fol[0:fol.rfind("/")]
	s=""; j=mainfolder.find("/")+1
	while True:
		j=fol.find("/",j)+1
		if j==-1: break
		s=fol[0:j-1]
		try: os.mkdir(s)
		except OSError as error: pass
		if s==g: break

def strpad(num,dgt,pad):
	nums=str(num)
	while len(nums)<dgt:
		nums=pad+nums
	return nums

def strpadc(num,dgt,pad):
	nums=str(num); t=bool(len(nums) and 1)
	while len(nums)<dgt:
		nums=(pad*t)+nums+(pad*(not t))
		t=bool(not t)
	return nums

def ctgpververify(s):
	p="0123456789."
	for i in range(len(s)):
		if p.find(s[i])<0: return 1
	l=p.split(".") # Versions are major.minor[.micro], only expected those
	if len(l)<2 or len(l)>3: return 1
	return 0

def fatErr(idx:int, fn:str="", fo:str=""):
	strl=[\
"""
File {} couldn't be downloaded.

Please make sure you're able to connect to GitHub and try again later.
""".format(fn),\
\
"""
Failed relocating a file.

From: {}
To: {}

This may stem from SD Card corruption or a heavily outdated build.
It's recommended to reinstall CTGP-7 at this point.
""".format(fo, fn),\
\
"""
The file method for {}
is unknown.

Is the file list corrupted, or did I miss a method?
Please contact CyberYoshi64 about this.

By the way, the update therefore fails.
""".format(fn),\
\
"""
The folder specified does not contain a valid CTGP-7 installation.

The version number of the installation is invalid.

Have you specified the correct folder? Have you even installed CTGP-7?
I will not guess; the update is aborted.
""".format(fn, fo)\
\
		 ]
	print("\x1b[?25h")
	try:
		clrscr(); print("\x1b[0;91m"+strl[idx])
	except: print("An unknown error occured. Please try again.")
	appexit(1)

def iff(x,i,o):
	if x: return i
	else: return o

def clrscr(): os.system(iff(os.name!="nt", "clear", "cls"))

def appexit(r: int):
	global mainfolder
	try: os.remove(mainfolder+"/changelog.txt")
	except: pass
	print("\x1b[0;0m\x1b[?25h")
	exit(r)

def dlErrCntCol():
	global rep; a=0
	if rep==0: a=90
	elif rep<5: a=93
	elif rep<15: a=91
	else: a=31
	return "\x1b[0;"+str(a)+"m"

def dlErrDesc():
	global rep
	return "Tries: "+str(rep+1)+"/30"

def splitChangelogData(filecnt: str):
	mode=0; arr=[]; vern=""; chng=""; char=""
	while filecnt.find(": :")>=0: filecnt=filecnt.replace(": :",":")
	while filecnt.find("::")>=0: filecnt=filecnt.replace("::",":")
	for idx in range(len(filecnt)):
		char=filecnt[idx]
		
		if char==":":
			mode+=1
			if mode>1: chng += "\n"
			continue
		if char==";":
			arr.append((vern,chng))
			vern=""; chng=""; mode=0
			continue
		
		if mode==0:
			vern += char
		else:
			chng += char
			
	if mode>0: arr.append((vern,chng))
	while arr.count(("","")): arr.remove(("",""))
	return arr

def fileMethodStrList(): return ["M","D","T"]

def parseAndSortDlList(dll):
	global dlCounter
	fileN=[]; fileM=[]; fileO=[]; newDl=[]; oldf=""
	dlCounter=0; filemode=fileMethodStrList()

	for i in range(len(dll)):
		ms=dll[i][0]
		mf=dll[i][1]

		if ms=="F":
			oldf=mf
		else:
			fileNC=-1
			try: 	fileNC=fileN.index(mf)
			except:
				fileN.append(mf); fileM.append(ms); fileO.append(oldf)
			else:
				fileN.pop(fileNC); fileM.pop(fileNC); fileO.pop(fileNC)
				fileN.append(mf); fileM.append(ms); fileO.append(oldf)
			oldf=""
	
	#for m in filemode:
	for i in range(len(fileN)):
			#if fileM[i]==m:
			if fileM[i]=="M": dlCounter += 1
			newDl.append((filemode.index(fileM[i]), fileN[i], fileO[i]))

	return newDl

def findCVerInCList(lst,ver):
	for idx in range(len(lst)):
		if lst[idx][0]==ver: break
	else: return 0 # 0.17.2 is broken
	return idx
def move (x, y): print("\033[%d;%dH" % (y, x))
def ScreenDisplay():
	global dlList, dlCounter, i, dlObtainedCnt, verf
	global oldtermw, oldtermh
	termw, termh = os.get_terminal_size()
	if (termw!=oldtermw or termh!=oldtermh) or (termw < 32 or termh < 10): clrscr()
	oldtermw, oldtermh = termw, termh
	lastver=verf[len(verf)-1][0]
	header="Updating to "+lastver
	fnm:str=dlList[i][1]
	fnm=fnm[fnm.rfind("/")+1:]
	while len(fnm)>termw-3: fnm="..."+fnm[4:]
	print("\x1b[?25l")
	move(0, 0) # clrscr()
	print("""{}\x1b[0;36m{}
{}

\x1b[0;93m{}
\x1b[0;37m{}

{}""".format("\n" * int((termh - 6) / 2 - 1), \
				 (header).center(termw-1),\
				 ("-"*len(header)).center(termw-1),\
				 strpadc(str(dlObtainedCnt)+"/"+str(dlCounter), termw-1, " "),\
				 fnm.center(termw-1),\
				 dlErrCntCol()+dlErrDesc().center(termw-1)))

def main():
	global mainfolder, ses, dlList, dlCounter, dlObtainedCnt
	global verf, vers, veri, i, rep, tooInstalled
	if len(argv)<2 or argv[1]=="-h":
		print("""CTGP-7 Updater script 1.0

Usage: {} <CTGP7fol>

CTGP-7fol – Path to CTGP-7 folder

This can refer to the CTGP-7 folder on your 3DS's SD Card or
a backup folder on your PC.

This tool acts as close to the official updater, so you have to make
sure, you specify the correct folder, otherwise, no updates will be
performed.""".format(argv[0]))
		exit()

	try: os.mkdir(mainfolder)
	except: pass

	try: verf=open(mainfolder+"/config/version.bin")
	except: fatErr(3)
	else:
		vers=verf.read(); verf.close()

		if len(vers)<3 or len(vers)>7: fatErr(3)
		if ctgpververify(vers): fatErr(3)
		print("CTGP-7 version detected: "+vers)


	url="https://raw.githubusercontent.com/PabloMK7/CTGP-7updates/master/updates/changeloglist"

	dl=ses.get(url)
	if not dl.ok:
		print("Failed getting changelog. Cannot update.")
		print("Please try again later.")
		exit(1)

	verf=splitChangelogData(dl.text)
	veri=findCVerInCList(verf,vers)

	try: os.stat(mainfolder+"/changelog.txt")
	except: pass
	else: os.remove(mainfolder+"/changelog.txt")
	of=open(mainfolder+"/changelog.txt","xb")

	for i in range(veri+1,len(verf)):
		of.write(bytes(""" --- Changelog for {} :

{}

""".format(verf[i][0],verf[i][1]),"utf8"))
		of.flush()

	print("Searching for updates...")

	percv0=len(verf)-veri-1
	for i in range(veri+1,len(verf)):
		url="https://github.com/PabloMK7/CTGP-7updates/releases/download/v"+verf[i][0]+"/filelist.txt"
		print(("\x1b[2K  (%5.1f%%)  Get file list for " % ((i-veri)/percv0*100))+verf[i][0]+" ...", end="\r", flush=True)
		for rep in range(30):
			try: dl=ses.get(url, timeout=5)
			except: print("Fail: Try {} of 30 failed: unknown reason".format(rep+1))
			else:
				if dl.ok: break
				print("Fail: Try {} of 30 failed with statcode {}".format(rep+1,dl.status_code))
			time.sleep(1.0)
		else:
			fatErr(0)
		dl=dl.text.split("\n")
		for i in dl:
			if i=="": break
			dlList.append((i[0],i[1:]))
	dlList=parseAndSortDlList(dlList)

	if len(dlList) or veri<len(verf)-1:
		print("\x1b[2KDo you want to update to "+verf[len(verf)-1][0]+"?")
		of.close(); os.system(iff(os.name!="nt","less "+mainfolder+"/changelog.txt", "notepad "+mainfolder+"/changelog.txt"))
		input("Press ^C to abort the update, otherwise press Return")
	else:
		print("No updates were found. Please try again later.")
		return 2

	try: ses.get("https://raw.githubusercontent.com/PabloMK7/CTGP-7updates/master/updates/data/")
	except: pass

	for i in range(len(dlList)):
		fmode=dlList[i][0]; fname=dlList[i][1]; fmvo=dlList[i][2]
		if fmode==fileMethodStrList().index("M"): rep=0; dlObtainedCnt += 1; ScreenDisplay()
		
		url="https://raw.githubusercontent.com/PabloMK7/CTGP-7updates/master/updates/data"+fname
		f=fname; f1=fmvo
		if fmode==0:
			
			mkfolders(mainfolder+f)
			
			for rep in range(30):
				try: dl=ses.get(url, timeout=5, allow_redirects=0)
				except: pass
				else:
					if dl.ok: break
				
				ScreenDisplay()
				time.sleep(1.0)
			else:
				fatErr(0,f,f1)
			
			of=open(mainfolder+f+".part","x+b")
			of.write(dl.content)
			of.flush()
			of.close()
			
			os.rename(mainfolder+f+".part",mainfolder+f)
		
		elif fmode==1:
			try: os.stat(mainfolder+f)
			except: pass
			else: os.remove(mainfolder+f)
		elif fmode==2:
			try: os.stat(mainfolder+f1)
			except: fatErr(1,f,f1)
			else:
				try: os.rename(src=mainfolder+f1, dst=mainfolder+f)
				except: fatErr(1,f,f1)
		else:
			fatErr(2,f,f1)

	try: os.stat(mainfolder+"/cia/tooInstall.cia")
	except: pass
	else:
		tooInstalled=True
		os.rename(src=mainfolder+"/cia/tooInstall.cia",dst=mainfolder+"/cia/CTGP-7.cia")
		os.rename(src=mainfolder+"/cia/tooInstall.3dsx",dst=mainfolder+"/cia/CTGP-7.3dsx")

	# Update config/version.bin
	if len(dlList):
		try: os.stat(mainfolder+"/config/version.bin")
		except: pass
		else: os.remove(mainfolder+"/config/version.bin")
		of=open(mainfolder+"/config/version.bin","x+b")
		of.write(verf[len(verf)-1][0].encode("ascii")); of.flush(); of.close()
	return 0
mainfolder=argv[1]
ses=requests.session()
dlList=[]; verf=0; vers=0; veri=0; i=0; rep=0; tooInstalled=False
dlCounter=0; oldtermw=0; oldtermh=0; dlObtainedCnt=0

try:
	print("\x1b[0;0m\x1b[?25h")
	if not main():
		clrscr()
		print("\n\x1b[0;92m Update successful!\x1b[0;0m")
		if tooInstalled:
			print("""
\x1b[0;96mThe launcher was updated.

\x1b[0;0mPlease install the new CTGP-7 CIA manually through FBI.

Open FBI and navigate SD > CTGP-7 > cia > CTGP-7.cia, then select "Install" and agree.
""")
except KeyboardInterrupt:
	clrscr()
	print("\x1b[0;91mThe program was interrupted. Update aborted.")
	appexit(5)
#except:
#	fatErr(0xDEADBEEF)

appexit(0)
