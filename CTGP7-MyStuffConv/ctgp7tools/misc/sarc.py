from struct import pack, unpack_from
from io import BytesIO, IOBase
from typing import Any
from ioHelper import IOHelper
import os

from ctgp7tools import vprint

class SFATEntry:
    _SIZE_ = 16
    
    def __init__(self, fd:IOHelper=None, dataOff=0, mul=101):
        self.mul = mul
        self.name = 0
        self.strOff = 0
        self.data = b''
        if fd:
            self.name = fd.readInt(32)
            self.strOff = fd.readInt(32)

            dataStart = fd.readInt(32)
            dataLength = fd.readInt(32) - dataStart

            fo = fd.getOffset()
            fd.setOffset(dataStart + dataOff)
            self.data = fd.readRaw(dataLength)
            fd.setOffset(fo)
    
    def pack(self, fd:IOHelper, off, mainOff):
        if type(self.name)==str:
            fd.writeInt(SARC.hash(self.name, self.mul), 32)
        else:
            fd.writeInt(self.name, 32)
        fd.writeInt(self.strOff, 32)
        fd.writeInt(off - mainOff, 32)

        pad = 7

        pad = (2**pad) - 1
        dataLen = len(self.data) + pad & ~pad
        fd.writeInt(off + len(self.data) - mainOff, 32)
        co = fd.getOffset()
        fd.setOffset(off)
        fd.writeRaw(self.data, dataLen)
        fd.getSize()
        fd.setOffset(co)

    def __lt__(self, other):
        if type(other)==type(self):
            if type(self.name)==str:
                self.name = SARC.hash(self.name, self.mul)
            if type(other.name)==str:
                other.name = SARC.hash(other.name, other.mul)
            return self.name < other.name
    
    def __repr__(self) -> str:
        return f"0x{self.name:08X}"

class SARC:
    class SFNT:
        _SIZE_ = 8

        def __init__(self, fd:IOHelper = None):
            self.unk1 = 0
            if fd:
                assert(fd.readRaw(4)==b'SFNT')
                fd.readInt(16)
                self.unk1 = fd.readInt(16)
        
        def pack(self, fd:IOHelper):
            fd.writeRaw(b'SFNT', 4)
            fd.writeInt(self._SIZE_, 16)
            fd.writeInt(self.unk1, 16)
    
    class SFAT:
        _SIZE_ = 0xC
        
        def __init__(self, fd:IOHelper = None, dataOff = 0):
            self.multiplier = 101
            self.nodes = []
            if fd:
                assert(fd.readRaw(4)==b'SFAT')
                fd.readInt(16)
                nodeCount = fd.readInt(16)
                self.multiplier = fd.readInt(32)

                for i in range(nodeCount):
                    self.nodes.append(SFATEntry(fd, dataOff, self.multiplier))
                self.nodes.sort()

        def getFile(self, name) -> SFATEntry:
            if type(name)==str:
                h = SARC.hash(name, self.multiplier)
            else:
                h = name
            
            for i in self.nodes:
                if type(i.name)==str:
                    i.name = SARC.hash(i.name, self.multiplier)
                if i.name == h: return i
            else:
                return None
        
        def remove(self, name):
            try:
                self.nodes.remove(self.getFile(name))
            except: pass
        
        def add(self, name, data):
            s = SFATEntry(mul=self.multiplier)
            s.name = SARC.hash(name, s.mul)
            s.data = data
            s.strOff = 0
            self.nodes.append(s)

        def calcsize(self):
            return self._SIZE_ + SFATEntry._SIZE_ * len(self.nodes)

        def pack(self, fd:IOHelper, dataOff:int):
            fd.writeRaw(b'SFAT', 4)
            fd.writeInt(self._SIZE_, 16)
            fd.writeInt(len(self.nodes), 16)
            fd.writeInt(self.multiplier, 32)

            off = dataOff
            self.nodes.sort()
            for i in self.nodes:
                i.pack(fd, off, dataOff)
                off = fd.getSize()

    sfnt = SFNT()
    sfat = SFAT()
    _HDR_SIZE_ = 20
    version = 256

    @staticmethod
    def hash(name, multiplier):
        hash = 0
        for i in name:
            hash = (hash * multiplier + ord(i)) & (2**32-1)
        return hash
    
    def hashName(self, name):
        if type(name)!=int:
            return SARC.hash(name, self.sfat.multiplier)
        else: return name
    
    def hasFile(self, name):
        return self.sfat.getFile(name)!=None

    def getFile(self, name):
        vprint(f"SARC.getFile: {name}")
        return self.sfat.getFile(name)
    
    def setFile(self, name, data, raiseErr=False):
        if not isinstance(data, IOBase):
            if type(data)==bytes:
                fd = BytesIO(data)
            else:
                if os.path.exists(data):
                    fd = open(data, "rb")
                elif raiseErr:
                    raise Exception("File doesn't exist: "+data)
                else:
                    return
        else:
            fd = data
        
        vprint(f"SARC.setFile: {name}")
        
        if self.hasFile(name):
            self.sfat.remove(name)
        
        self.sfat.add(name, fd.read())

    def __init__(self, data=None, key=101):
        if data:
            self.load(data)
        else:
            self.sfat = SARC.SFAT()
            self.sfnt = SARC.SFNT()

    def load(self, data):
        if not isinstance(data, IOHelper):
            f = IOHelper(data, False)
        else:
            f = data
        
        assert(f.readRaw(4)==b"SARC")
        f.readInt(16)
        f.readBOM()
        assert(f.getSize() >= f.readInt(32))
        dataOff = f.readInt(32)
        self.version = f.readInt(16)
        assert(self.version == 0x100)
        f.readRaw(2)

        self.sfat = SARC.SFAT(f, dataOff)
        self.sfnt = SARC.SFNT(f)

    def pack(self, fd:IOHelper):
        vprint(f"Packing SARC to {fd.name if hasattr(fd,'name') else '<bytes>'}...")
        fd.setSize(0)
        dataOff = (self._HDR_SIZE_ + self.sfat.calcsize() + self.sfnt._SIZE_ + 255) & ~255
        
        fd.writeRaw(b'SARC', 4)
        fd.writeInt(self._HDR_SIZE_, 16)
        fd.writeBOM()
        fd.writeInt(0, 32)
        fd.writeInt(dataOff, 32)
        fd.writeInt(self.version, 16)
        fd.writeInt(0, 16)

        self.sfat.pack(fd, dataOff)
        self.sfnt.pack(fd)

        fd.getSize()
        fd.setOffset(8)
        fd.writeInt(fd.getSize(), 32)

    def __repr__(self) -> str:
        return f"<SARC version={self.version}, nodes={self.sfat.nodes}>"