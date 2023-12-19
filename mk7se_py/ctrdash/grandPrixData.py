"""
### GrandPrixData

2023 CyberYoshi64

- [Source: MK7 Wiki](https://mk3ds.com/index.php?title=Save_File#GrandPrixData)
"""

class GrandPrixData:
    _TROPHYTYPE = (
        "None", "Bronze", "Silver", "Gold",
        "Invalid"
    )
    _RANKTYPE = (
        "None", "C", "B", "A",
        "1*", "2*", "3*",
        "Invalid"
    )

    def __init__(self, data=None):
        if data: self.load(data)
    
    def load(self, data):		
        self.entries = []
        for i in data:
            self.entries.append([
                bool(i&1), (i>>4)&15, (i>>1)&7
            ])
    
    def setCompleted(self, index, value):
        if index<0 or index>=len(self.entries): return
        self.entries[index][0]=bool(value)
    def setTrophy(self, index, value):
        if index<0 or index>=len(self.entries): return
        self.entries[index][1]=(value & 15)
    def setRank(self, index, value):
        if index<0 or index>=len(self.entries): return
        self.entries[index][2]=(value & 7)
    def setEntry(self, index, trophy=None, rank=None, completed=None):
        if trophy!=None: self.setTrophy(index, trophy)
        if rank!=None: self.setRank(index, rank)
        if completed!=None: self.setCompleted(index, completed)
    
    def pack(self):
        b = b''
        for i in self.entries:
            b += bytes.fromhex(f"{i[0]&1|(i[1]&15)<<4|(i[2]&7)<<1:02X}")
        return b
    
    def __str__(self):
        s = f"<{__name__} ["
        for i in self.entries:
            s += f"<completed={i[0]}, trophy='{self._TROPHYTYPE[min(len(self._TROPHYTYPE)-1,i[1])]} (0x{i[1]:X})', rank='{self._RANKTYPE[min(len(self._RANKTYPE)-1,i[2])]} (0x{i[2]:X})'>"
        return s+"]>"