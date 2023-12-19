from .crc16_ccitt import CRC16
import struct

class CTRFaceData:
	"""
	CFCD / CFSD data parser
	
	CFCD (CTR Face Core Data) contains all properties of a Mii, including Mii Maker context
	CFSD (CTR Face Store Data) is used by games, whereas an additional checksum is appended to the data to verify that standalone Mii's integrity
	
	Note that the checksum of a CFSD (or within the CFL_DB) is big-endian, despite the format itself being little-endian.
	"""
	_STRUCT = ">BBBBQI6s2xH20sBBB23s20s"
	_PLATFORM = (
		("UNK","Unknown"),
		("RVL","Wii"),
		("NTR","DS / DSi"),
		("CTR","3DS"),
		("WUP","Wii U / Switch")
	)
	PLATFORM = {
		"RVL": 1,
		"NTR": 2,
		"TWL": 2,
		"CTR": 3,
		"WUP": 4,
		"NX": 5,
	}
	_REGLOCK = (
		("NONE","No lock"),
		("JPN","Japan"),
		("USA","America"),
		("EUR","Europe")
	)
	REGLOCK = {
		"NONE": 0,
		"JPN": 1,
		"USA": 2,
		"EUR": 3,
	}
	_CHARSET = (
		"JPN+USA+EUR",
		"CHN",
		"KOR",
		"TWN"
	)
	CHARSET = {
		"JPN": 0,
		"USA": 0,
		"EUR": 0,
		"std": 0,
		"CHN": 1,
		"KOR": 2,
		"TWN": 3
	}
	_TYPE = (
		"CFCD",
		"CFSD"
	)
	TYPE = {
		"CFCD": False,
		"CFSD": True
	}
	version = 3
	copyable = False
	profanity = False
	regionLock = 0
	charSet = 0
	pageIdx = 0
	slotIdx = 0
	unk1 = 0
	platform = 3
	systemID = 0
	miiID = 0
	creatorMAC = 0
	miiProps1 = 0 # stub for now
	miiName = ""
	weight = 0
	height = 0
	sharable = False
	unk2 = 0
	miiProps2 = b'' # stub for now
	authorName = ""
	type = False # False=CFCD / True=CFSD
	isValid = True # only substantial for CFSD
	
	def __init__(self, data=None, failOnErr=True):
		if data: self.load(data, failOnErr)
	
	def load(self, data, failOnError=True):
		self.version, bm1, bm2, bm3, self.systemID, self.miiID, \
		self.creatorMAC, self.miiProps1, self.miiName, self.weight, \
		self.height, bm4, self.miiProps2, self.authorName = \
			struct.unpack_from(self._STRUCT, data[:92])
		
		if self.version != 3 and failOnError: raise Exception(f"Mii data is of unknown version: {self.version}")
		isValid = True # No checksum, unless...
		if len(data)>=96: # it's a CFSD which has a checksum at the end
			crc = int.from_bytes(data[94:96],"big")
			crc2 = CRC16(data[:94])
			self.type = True
			self.isValid = crc == crc2.digest()
		
		self.copyable = bool(bm1 & 1)
		self.profanity = bool(bm1 & 2)
		self.regionLock = (bm1 >> 2) & 3
		self.charSet = (bm1 >> 4) & 3
		self.pageIdx = (bm2 >> 0) & 15
		self.slotIdx = (bm2 >> 4) & 15
		self.unk1 = (bm3 >> 0) & 15
		self.platform = (bm3 >> 4) & 7
		self.unk2 = (bm4 >> 1) & 127
		self.sharable = not bool(bm4 & 1)
		self.miiName = self.miiName.decode("utf-16-le","replace")
		self.authorName = self.authorName.decode("utf-16-le","replace")
	
	def pack(self, asCFSD=True):
		b = struct.pack(
			self._STRUCT,
			3,
			
			(self.copyable & 1)|\
			(self.profanity & 1)<<1|\
			(self.regionLock & 3)<<2|\
			(self.charSet & 3)<<2,
			
			(self.pageIdx & 15)|\
			(self.slotIdx & 15)<<4,
			
			(self.unk1 & 15)|\
			(self.platform & 7)<<4,
			
			self.systemID, self.miiID, self.creatorMAC,
			self.miiProps1,
			self.miiName.encode("utf-16-le","replace"),
			self.weight, self.height,
			
			(not self.sharable & 1)|\
			(self.unk2 & 127)<<1,
			
			self.miiProps2, self.authorName.encode("utf-16-le","replace")
		)
		if asCFSD:
			b += b'\0\0'
			crc = CRC16(b)
			b += int.to_bytes(crc.digest(),2,"big")
		return b

	def calcTime(self):
		off = (self.miiID & (2**28-1)) * 2
		# print(off + 1262304000) # Debug printing Unix time to help my sanity
		
		"""Could've passed into datetime but where's the fun, eh?"""
		sec = off % 60; min = off//60; hour = min//60 % 24
		day = min//1440 + 730; 	# While the first date is 2010, I'm rounding down to 2008
								# to simplify leap year calculations
		min %= 60; year = (day//1461)*4
		day = day % 1461
		year += day//365
		day = day % 365
		month = 0
		while True:
			dpm = [31,28+bool(not(year & 3)),30,31,30,31,31,30,31,30,31,31][month]
			if day < dpm: break
			day -= dpm
			month += 1
		return f"{year+2008:4d}/{month+1}/{day+1}, {hour}:{min:02d}:{sec:02d}"
	
	def str(self):
		i = self.miiName.find('\0'); miiName = self.miiName[:i] if i>=0 else self.miiName
		i = self.authorName.find('\0'); authorName = self.authorName[:i] if i>=0 else self.authorName
		return f"""\
type = {self._TYPE[self.type]}
isValid = {self.isValid}
version = {self.version}
sharable = {self.sharable}
copyable = {self.copyable}
miiName = "{miiName}"
authorName = "{authorName}"
profanity = {self.profanity}
platform = {self.platform} ({self._PLATFORM[self.platform][1]})
systemID = {self.systemID}
miiID = {self.miiID} ({self.calcTime()})
regionLock = {self.regionLock} ({self._REGLOCK[self.regionLock][0]})
charSet = {self.charSet} ({self._CHARSET[self.charSet][0]} - {self._CHARSET[self.charSet][1]})
Mii Maker position : Page {self.pageIdx}, Slot {self.slotIdx}
"""
	
	def __str__(self):
		i = self.miiName.find('\0'); miiName = self.miiName[:i] if i>=0 else self.miiName
		i = self.authorName.find('\0'); authorName = self.authorName[:i] if i>=0 else self.authorName
		return f"<{__name__} type={self._TYPE[self.type]}, isValid={self.isValid}, sharable={self.sharable}, copyable={self.copyable}, miiName='{miiName}', authorName='{authorName}', creationDate='{self.calcTime()}', charSet={self._CHARSET[self.charSet]}>"
	
	def __repr__(self): return str(self)
