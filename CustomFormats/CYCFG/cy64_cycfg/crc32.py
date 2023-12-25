"""
### CRC32 (taken from MK7)

2023 CyberYoshi64

- [Source: Marc Robledo's MK7 Save Editor](https://github.com/marcrobledo/savegame-editors/blob/master/mario-kart-7/mario-kart-7.js#L31-L52)
"""

class CRC32:
    table = []
    result = 2**32-1
    
    def __init__(self, data=None):
        self.table = []
        for n in range(256):
            c = n
            for k in range(8): c = (0xEDB88320^(c>>1)) if (c&1) else (c>>1)
            self.table.append(c)
        if data:
            self.append(data)
    def append(self, data):
        crc = self.result
        for i in range(len(data)):
            crc = (crc >> 8) ^ self.table[(crc ^ data[i]) & 255]
        self.result = crc
        return self
    def digest(self):
        return self.result ^ -1 & (2**32-1)