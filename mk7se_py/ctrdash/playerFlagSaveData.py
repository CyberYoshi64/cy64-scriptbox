"""
### PlayerFlagSaveData

2023 CyberYoshi64

- [Source: MK7 Wiki](https://mk3ds.com/index.php?title=Save_File#PlayerFlagSaveData)
- [Source: hax0kartik's MK7 Save Editor](https://github.com/hax0kartik/Mk7se/blob/master/source/include/offset.h#L2-L11)

NOTE: The majority of this section is undocumented and thus taken by dummy class members
"""

import struct

class OpponentMask:
    entries = []

    def __init__(self, data) -> None:
        self.entries = []
        for i in data:
            self.entries.append(i)
    def pack(self):
        return bytes(self.entries)

class PlayerFlagSaveData:
    _STRUCT = "< 856s I 504s I 12s 3I H I 7H 12s 100s 524s"
    
    def __init__(self, data=None):
        if data: self.load(data)
    def load(self, data):
        self.prefix, self.coins, self.unk2, self.cecMeets, \
        self.unk3, self.wins, self.losses, bm1, self.unk4, self.chars, \
        self.charUnlocks, self.karts, self.kartUnlocks, self.tires, \
        self.tireUnlocks, self.gliders, self.gliderUnlocks, \
        self.unk5, self.opponentMask, \
        self.suffix = \
            struct.unpack(self._STRUCT, data)
        self.vr = (bm1>>0) & 131071
        self.unk7 = (bm1 >> 17) & 127
        self.cups = (bm1 >> 24) & 255
        self.opponentMask = OpponentMask(self.opponentMask)
    def pack(self):
        return struct.pack(
            self._STRUCT,
            self.prefix, self.coins & (2**32-1), self.unk2,
            self.cecMeets & (2**32-1),
            self.unk3, self.wins & (2**32-1), self.losses & (2**32-1),
            (self.vr & 131071) | (self.unk7 & 127)<<17 | (self.cups & 255)<<24,
            self.unk4, self.chars, self.charUnlocks,
            self.karts, self.kartUnlocks, self.tires,
            self.tireUnlocks, self.gliders, self.gliderUnlocks,
            self.unk5, self.opponentMask.pack(), self.suffix
        )
    def __str__(self):
        return f"<{__name__} coins={self.coins}, cecMeets={self.cecMeets}, wins={self.wins}, losses={self.losses}, vr={self.vr}, cups={self.cups:02X}, chars={self.chars:04X}, charUnlocks={self.charUnlocks:04X}, karts={self.karts:04X}, kartUnlocks={self.kartUnlocks:04X}, tires={self.tires:04X}, tireUnlocks={self.tireUnlocks:04X}, gliders={self.gliders:04X}, gliderUnlocks={self.gliderUnlocks:04X}, opponentMask={self.opponentMask.entries}>"
    def __repr__(self): return str(self)
