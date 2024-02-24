#!/usr/bin/python3

import os, re, io, argparse, urllib3, shutil, glob

KEEP_CDN_CONTENT = False

urlmgr = urllib3.PoolManager()

server = "http://nus.cdn.c.shop.nintendowifi.net/ccs/download/"
ninupdate = "http://yls8.mtheall.com/ninupdates/titlelist.php?csv=1&sys="
sysarr = ["ctr",  "ktr"]
yls = None
arg = None

def vprint(*s):
	if arg.verbose: print(*s)

class YLS_Sysver:
	def __init__(self):
		self.intstr = ""
		self.major = 0
		self.minor = 0
		self.micro = 0
		self.rev = 0
	
	def rebuild(self):
		self.intstr = f"{self.major}.{self.minor}.{self.micro}-{self.rev}"
	
	def setLabel(self, value):
		self.major = int(value[0])
		self.minor = int(value[1])
		self.micro = int(value[2])
		self.rev = int(value[3])
		self.rebuild()
	def setMajor(self, value): self.major = value
	def setMinor(self, value): self.minor = value
	def setMicro(self, value): self.micro = value
	def setRevision(self, value): self.rev = value
	
	def compare(self, other):
		if (self.major < other.major): return -1
		if (self.major > other.major): return 1
		if (self.minor < other.minor): return -1
		if (self.minor > other.minor): return 1
		if (self.micro < other.micro): return -1
		if (self.micro > other.micro): return 1
		if (self.rev == 999 or other.rev == 999): return 0
		if (self.rev < other.rev): return -1
		if (self.rev > other.rev): return 1
		return 0
	
	def __lt__(self, other): return self.compare(other) == -1
	def __gt__(self, other): return self.compare(other) == 1
	def __eq__(self, other): return self.compare(other) == 0
	def __ne__(self, other): return self.compare(other) != 0
	def __ge__(self, other): return self.compare(other) != -1
	def __le__(self, other): return self.compare(other) != 1
	def __str__(self): return self.intstr

class YLS_Titlever:
	def __init__(self):
		self.version = 0
		self.sysver = YLS_Sysver()
	
	def __str__(self): return f"v{self.version} {self.sysver}"
	def __repr__(self): return str(self)

class YLS_Title:
	def __init__(self):
		self.id = 0
		self.ver = []
	
	def __repr__(self): return f"<YLS_Title id={self.id:016X}, ver={self.ver}>"

class YLS:
	regions = {}
	
	def __init__(self, file=None) -> None:
		self.regions = {}
		if file: self.Import(file)
	
	def Entry(self, region, title):
		if not region in self.regions:
			self.regions[region] = []
		
		self.regions[region].append(title)
	
	def Import(self, data):
		with io.BytesIO(data) as fd:
			size = fd.seek(0,2)
			fd.seek(0)
			fd.readline()
			while fd.tell() < size:
				line = fd.readline().strip().decode("utf-8").split(",")
				if len(line) != 4: continue
				
				t = YLS_Title()
				t.id = int(line[0], 16)
				
				if (t.id == 0x4013000001B02): line[3] = line[3].replace("_GPIO", " GPIO").replace("02-11-15 GPIO", "9.5.0-22")
				if (t.id == 0x400102002CA00): line[3] = line[3].replace("_JPN", " JPN").replace("10-02-14 JPN", "9.1.0-20J")
				
				if (line[1] == "TWN"): line[3] = line[3].replace("08-18-16_TWN_BeginScanning", "11.0.0-33T").replace("N/A", "11.3.1-36T")
				
				mat = re.findall(r"(\d+)\.(\d+)\.(\d+)-(\d+)", line[3])
				matIdx = 0
				
				for ver in line[2].split(" "):
					tv = YLS_Titlever()
					tv.version = int(ver[1:])
					tv.sysver.setLabel(mat[matIdx])
					t.ver.append(tv)

					matIdx += 1
				
				if mat: self.Entry(line[1][0], t)
	
def downloadFile(url, path) -> int:
	fails = 5
	badStatus = 0
	while fails:
		try:
			u = urlmgr.request("GET", url, preload_content=False)
			
			if u.status != 200:
				badStatus = u.status
				break
			
			with open(path, "wb") as f:
				f.truncate(0)
				while True:
					c = u.read(32768)
					if c==b'': break
					f.write(c)
		except Exception as e:
			if type(e) == KeyboardInterrupt: fails = 0
			if os.path.exists(path): os.remove(path)
			vprint(f"Attempt {6-fails}/5 failed: {str(e)}")
		else:
			return 0
		fails -= 1
	if badStatus: raise Exception(f"Returned status code {badStatus}")
	return 1
	
def downloadData(url) -> bytes:
	fails = 5
	badStatus = 0
	while fails:
		try:
			with urlmgr.request("GET", url, preload_content=False) as u:
				
				if u.status != 200:
					badStatus = u.status
					break
				
				return u.read()
		except Exception as e:
			if type(e) == KeyboardInterrupt: fails = 0
			vprint(f"Attempt {6-fails}/5 failed: {str(e)}")
		else:
			return 0
		fails -= 1
	if badStatus: raise Exception(f"Returned status code {badStatus}")
	return 1

def ctrver(ver:int):
	return f"{(ver>>10)&63}.{(ver>>4)&63}.{(ver>>0)&15}"

def singleDownload(id, ver, path):
	
	global server
	
	title = f"{id:016X}"
	vprfx = f"{id:016X}.{ver:04X}" if ver>=0 else title
	ftmp  = f"{path}.tmp"
	dtmd  = f"{server}{title}/tmd.{ver}"
	dtmdn = f"{server}{title}/tmd"
	dcetk = f"{server}{title}/cetk"
	
	res = 0
	
	os.makedirs(ftmp, exist_ok=True)
	
	try:
		vprint(f"{vprfx}: Downloading TMD")
		res = downloadFile(dtmd if ver>0 else dtmdn, os.path.join(ftmp, "tmd"))
		if res: return res
		vprint(f"{vprfx}: Downloading CETK")
		res = downloadFile(dcetk, os.path.join(ftmp, "cetk"))
		if res: return res
	except:
		shutil.rmtree(ftmp)
		raise Exception(f"{title} v{ctrver(ver)} doesn't exist on CDN.")
		
	tmd = None
	try:
		tmd = open(os.path.join(ftmp, "tmd"),"rb")
		tmd.seek(518)
		cc = int.from_bytes(tmd.read(2),"big")
		for i in range(cc):
			contentOff = 2820 + 48 * i
			tmd.seek(contentOff)
			cid = int.from_bytes(tmd.read(4),"big")
			vprint(f"{vprfx}: Downloading content {cid:08X} ({i+1}/{cc})")
			res = downloadFile(f"{server}{title}/{cid:08x}", os.path.join(ftmp, f"{cid:08x}"))
			if res:
				shutil.rmtree(ftmp)
				return res
	except Exception as e:
		if tmd: tmd.close()
		shutil.rmtree(ftmp)
		raise Exception(f"Title {title} v{ctrver(ver)} failed to download: {e}")
		return 1
	
	if tmd: tmd.close()
	
	vprint(f"Building CIA for {title} v{ctrver(ver)}")
	res = os.system('make_cdn_cia "{}" "{}"'.format(ftmp, f"{path}.cia"))
	
	if not KEEP_CDN_CONTENT: shutil.rmtree(ftmp)
	return res

def firmwdownload(sys, region, path):
	global yls
	if not region in yls.regions:
		raise Exception(f"Invalid region! Valid options are {list(yls.regions.keys())}")
	
	index = 0
	length = len(yls.regions[region])
	for t in yls.regions[region]:
		optimal = None
		
		for tv in t.ver:
			if tv.sysver == sys:
				optimal = tv
				break
			
			if (tv.sysver < sys and (optimal == None or tv.sysver > optimal.sysver)): optimal = tv
		print(f" - {sys.intstr}{region}: {index+1}/{length} ({t.id:016X})")
		if optimal == None: continue
		if singleDownload(t.id, optimal.version, os.path.join(path, f"{t.id:016X}")): return
		index += 1

argp = argparse.ArgumentParser()
argp.add_argument("-s", "--system", metavar="sys", default="ctr", help="System to download for (CTR/KTR)")
argp.add_argument("-f", "--firmver", action="append", metavar="fw", help="Firmware version to download")
argp.add_argument("-t", "--title", action="append", metavar="id.ver", help="Title and version to download")
argp.add_argument("-c", "--clean", action="append", help="Clean folder for system")
argp.add_argument("-v", "--verbose", action="store_true", help="Enable console output")

arg = argp.parse_args()
arg.system = arg.system.lower()

if not arg.system in sysarr:
	print("The specified system is not allowed. Here's a list of supported systems:")
	print(sysarr)
	argp.print_usage()
	exit(1)

if not arg.firmver and not arg.title and not arg.clean:
	print("A firmware version or a title must be specified")
	argp.print_usage()
	exit(255)

hadError = False
isKTR = arg.system == "ktr"

if arg.firmver:
	vprint(f"Downloading YLS for {arg.system}")
	yls = YLS(downloadData(ninupdate + arg.system))
	vprint()
	for i in arg.firmver:
		path = ""
		try:
			firmver = i.strip()
			match = re.compile("(\d+)\.(\d+)(\.(\d+))?(-(\d+))?([a-zA-Z])+").match(firmver)
			if match:
				firmw = YLS_Sysver()
				firmw.setLabel([match[1], match[2], match[4] if match[4] else "9", match[6] if match[6] else "999"])
				region = match.group(7).upper()
				print(f"Downloading firmware {firmw}{region}")
				path = "{}{}".format(firmw.intstr, region[0])
				firmwdownload(firmw, region[0], path)
			else:
				raise Exception("Bad firmware version specified.")
		except KeyboardInterrupt:
			if path:
				l = glob.glob(f"{path}{os.sep}*{os.sep}")
				for i in l:
					shutil.rmtree(i, ignore_errors=True)
			print("User cancelled operation")
			exit(2)
		except Exception as e:
			print(f"Failed downloading firmware {firmver}: {e}")
			if path:
				l = glob.glob(f"{path}{os.sep}*{os.sep}")
				for i in l:
					shutil.rmtree(i, ignore_errors=True)
			hadError = True
		vprint()

if arg.title:
	for i in arg.title:
		path = None
		try:
			try:
				title = i.strip().split(".")

				try:    title[0] = int(title[0].strip(),16)
				except: title[0] = int(title[0].strip(),0)
				
				if (title[0] < 0x0004000000000000) or (title[0] > 0x00048FFFFFFFFFFF): raise Exception("Title ID is malformed")

				title[1] = int(title[1].strip(),0)
				if (title[1] < 0) or (title[1] > 65535): raise Exception("Title version is out of bounds")
			except:
				try:
					title = i.strip()
					try:    title = int(title,16)
					except: title = int(title,0)
					if (title < 0x0004000000000000) or (title > 0x00048FFFFFFFFFFF): raise Exception("Title ID is malformed")
					title = [title, -1]
				except Exception as e:
					raise Exception("Malformed title specifier: "+str(e))
			print(f"Downloading {title[0]:016X} v{ctrver(title[1])}")
			path = f"{title[0]:016X}.{title[1]:04X}" if title[1]>=0 else f"{title[0]:016X}"
			singleDownload(title[0], title[1], path)
		except KeyboardInterrupt:
			if path: shutil.rmtree(path)
			print("User cancelled operation")
			exit(2)
		except Exception as e:
			if path: shutil.rmtree(path)
			print(str(e))
			hadError = True
		vprint()

if arg.clean:
	for i in arg.clean:
		for j in glob.glob(i+"/*.cia"):
			t = int(j[-20:-4],16)
			if t & 0x0000000020000000:
				if not isKTR:
					vprint(f"Removed {j}")
					os.remove(j)
			else:
				if isKTR:
					u = f"{i}/{t | 0x0000000020000000:016X}.cia"
					if os.path.exists(u):
						vprint(f"Removed {j}")
						os.remove(j)

exit(hadError)
