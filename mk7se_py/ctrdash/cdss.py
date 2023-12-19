"""
### CTR Dash System Save

2023 CyberYoshi64

- [Source: MK7 Wiki](https://mk3ds.com/index.php?title=Save_File)
"""

import struct, io
from ctr.mii.facedata import CTRFaceData
from .crc32 import CRC32
from .grandPrixData import GrandPrixData
from .opponentList import OpponentList
from .playerFlagSaveData import PlayerFlagSaveData
from .rankingSaveData import RankingSaveData

class CDSS:
    _SIGN = b'SSDC' # CDSS in LE
    _STRUCT = "< 4s H 2B 96s 16s 32s H 78s 9I 1536s 32s I 16800s 2048s"
    
    isValid = False # CRC32
    
    def __init__(self, f=None, errorIfInvalid=False):
        self.new()
        if f: self.load(f, errorIfInvalid)
    
    def new(self):
        self.isValid = None
        self.field_0004 = 5
        self.field_0006 = 3
        self.field_0007 = 0
        self.miiData = CTRFaceData()
        self.field_0068 = b''
        self.cec_comment = ""
        self.field_0098 = 0
        self.field_009a = b''
        self.field_00e8 = 0
        self.field_00ec = 0
        self.field_00f0 = 0
        self.field_00f4 = 0
        self.field_00f8 = 0
        self.field_00fc = 0
        self.field_0100 = 0
        self.field_0104 = 0
        self.field_0108 = 0
        self.ranking = RankingSaveData()
        self.trophy = GrandPrixData()
        self.field_072c = 0
        self.opponents = OpponentList()
        self.flagData = PlayerFlagSaveData()
        self.flagData.vr = 1000

    def load(self, f, errorIfInvalid=False):
        if hasattr(f, "read"): fd = f
        else: fd = io.BytesIO(f)
        
        data = fd.read(0x50D0)
        if len(data)<0x50D0:
            if errorIfInvalid: raise IndexError("The file is truncated")
            return
        self.isValid = False
        signature, self.field_0004, self.field_0006, self.field_0007, \
        self.miiData, self.field_0068, self.cec_comment, self.field_0098, \
        self.field_009a, self.field_00e8, self.field_00ec, self.field_00f0, \
        self.field_00f4, self.field_00f8, self.field_00fc, self.field_0100, \
        self.field_0104, self.field_0108, self.ranking, self.trophy, \
        self.field_072c, self.opponents, self.flagData = \
            struct.unpack_from(self._STRUCT, data)
        assert signature == self._SIGN
        crc1 = CRC32(data)
        crc1 = int.to_bytes(crc1.digest(),4,"little")
        self.isValid = (crc1 == fd.read(4))
        if errorIfInvalid and not self.isValid: raise Exception("CDSS CRC check failed")
        
        self.cec_comment = self.cec_comment.decode("utf-16-le","replace").strip("\0")
        self.miiData = CTRFaceData(self.miiData, False)
        if errorIfInvalid and not self.miiData.isValid: raise Exception("Mii CFSD CRC check failed")
        if errorIfInvalid and not self.miiData.type: raise Exception("Mii data appears to not be a CFSD")
        self.ranking = RankingSaveData(self.ranking)
        self.trophy = GrandPrixData(self.trophy)
        self.opponents = OpponentList(self.opponents)
        self.flagData = PlayerFlagSaveData(self.flagData)
    
    def pack(self):
        b = struct.pack(
            self._STRUCT,
            self._SIGN, self.field_0004, self.field_0006,
            self.field_0007, self.miiData.pack(), self.field_0068,
            self.cec_comment.encode("utf-16-le","replace"),
            self.field_0098, self.field_009a, self.field_00e8,
            self.field_00ec, self.field_00f0, self.field_00f4,
            self.field_00f8, self.field_00fc, self.field_0100,
            self.field_0104, self.field_0108,
            self.ranking.pack(), self.trophy.pack(),
            self.field_072c, self.opponents.pack(), self.flagData.pack()
        )
        crc1 = CRC32(b)
        b += int.to_bytes(crc1.digest(),4,"little")
        return b
    
    def __str__(self):
        return f"<{__name__} isValid={self.isValid}>"
    
    def __repr__(self): return str(self)
