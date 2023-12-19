"""
### OpponentList

2023 CyberYoshi64

- [Source: MK7 Wiki](https://mk3ds.com/index.php?title=Save_File#OpponentList)

- [Additional info: CountryCode/AreaCode](https://docs.google.com/spreadsheets/d/1mSAomO_msfNllNsPeXbgU6UbJaGV5t6NvbZi6ebPFx4/htmlview)
"""

import struct
from ctr.mii.facedata import CTRFaceData

class OpponentData:
    _STRUCT = "<Q 5I 6H 20s 3H 2B 96s I"

    active = 0			# bool marking end of list?
    vr = 0				# Never shown in-game
    wins = 0			# Never shown in-game
    losses = 0			# Never shown in-game
    ownLosses = 0
    ownWins = 0
    unlockedChars = 0 	# Never shown in-game
    unlockedKarts = 0 	# Never shown in-game
    unlockedTires = 0	# Never shown in-game
    unlockedGliders = 0 # Never shown in-game
    unk2 = 0
    unk3 = 0
    unk4 = b'' 		# Very likely some form of user ID
    countryCode = 0 # Country Code (refer to 3dbrew)
    globLati = 0  	# Globe Latitude (from Area Code)
    globLongi = 0	# Globe Longitude (from Area Code)
    areaCode = 0	# Area Code (to be documented)
    unk5 = 0		# Unknown
    miiData = CTRFaceData()
    unk6 = 0		# set to 1 — if 0, Mii name is reset
    
    def __init__(self, data=None):
        if data: self.load(data)
    def load(self, data):
        self.active, self.vr, self.wins, self.losses, self.ownLosses, \
        self.ownWins, self.unlockedChars, self.unlockedKarts, self.unlockedTires, \
        self.unlockedGliders, self.unk2, self.unk3, self.unk4, self.countryCode, \
        self.globLati, self.globLongi, self.areaCode, self.unk5, self.miiData, \
        self.unk6 = \
            struct.unpack_from(self._STRUCT, data)
        
        self.miiData = CTRFaceData(self.miiData, False)
        
    def pack(self):
        return struct.pack(
            self._STRUCT,
            self.active, self.vr,
            self.wins & (2**32-1), self.losses & (2**32-1),
            self.ownLosses & (2**32-1), self.ownWins & (2**32-1),
            self.unlockedChars, self.unlockedKarts, self.unlockedTires,
            self.unlockedGliders, self.unk2, self.unk3, self.unk4, self.countryCode,
            self.globLati & (2**16-1), self.globLongi & (2**16-1),
            self.areaCode, self.unk5, self.miiData.pack(), self.unk6
        )
    def __str__(self):
        return f"<{__name__} vr={self.vr}, wins={self.wins}, losses={self.losses}, ownLosses={self.ownLosses}, ownWins={self.ownWins}, country={self.country}, globLati={self.globLati}, globLongi={self.globLongi}, miiData={self.miiData}, active={self.active}>"
    def __repr__(self): return str(self)

class OpponentList:
    _ENTRIES = 100
    _STRUCT_SIZE = struct.calcsize(OpponentData._STRUCT)
    entries : list[OpponentData] = []

    def __init__(self, data=None):
        if data: self.load(data)
    def load(self, data):
        self.entries = []
        off = 0
        for i in range(self._ENTRIES):
            self.entries.append(OpponentData(data[off:]))
            off += self._STRUCT_SIZE
    def pack(self):
        b = b''
        for i in self.entries:
            b += i.pack()
        return b
    def __str__(self):
        return f"<CTRDash__OpponentList entries={self.entries}>"
    def __repr__(self): return str(self)

