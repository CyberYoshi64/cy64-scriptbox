from struct import pack, unpack_from
from io import BytesIO, IOBase
from typing import Any
from ioHelper import IOHelper
import os
from hashlib import sha256

from ctgp7tools import vprint

def nametrunc(s:str):
    r = 0
    r = s.rfind(os.sep, 0, r-1)
    r = s[s.rfind(os.sep, 0, r-1)+1:]
    if len(s)!=len(r): r = ".../"+r
    return r

class SAHT:
    def __init__(self, data=None):
        self.key = 101 # It's not defined here, is SAHT a custom format?
        self.hashes = dict()
        self.alignment = 0x10
        if data is None:
            return
        elif type(data) is dict:
            self.hashes = data
            return
        elif isinstance(data, IOBase):
            fd = IOHelper(data)
        elif type(data) is IOHelper:
            fd = data
        else:
            fd = IOHelper(BytesIO(data))
        
        assert(fd.readRaw(4)==b'SAHT')
        size = fd.readInt(32)
        self.alignment = fd.readInt(32)
        count = fd.readInt(32)
        curOffset = 0x10
        i = 0
        while curOffset < size and i < count:
            chash = fd.readInt(32)
            cname = fd.readRawTillNull(self.alignment, 4).decode("utf-8","ignore").strip("\0")
            self.hashes[chash] = cname
            i += 1
    def getHash(self, key):
        h = SARC.hash(key, self.key)
        return h if (h in self.hashes) else 0
    def getAddHash(self, key):
        h = SARC.hash(key, self.key)
        if not h in self.hashes:
            self.hashes[h] = key
        return h
    def remove(self, key):
        if type(key) is str:
            h = SARC.hash(key, self.key)
        else:
            h = key
        self.hashes.pop(h,None)
    def add(self, key):
        h = SARC.hash(key, self.key)
        self.hashes[h] = key
    def verify(self, action=""):
        out = True
        removeKey = action=="remove"
        fixHash = action=="fix"
        badKeys = []
        for h,n in self.hashes.items():
            nh = SARC.hash(n, self.key)
            if h != nh:
                out = False
                badKeys.append(h)
        
        for h in badKeys:
            if removeKey:
                print(f"SAHT: Removed key {h:08X}({self.hashes[h]})")
                self.hashes.pop(h)
            if fixHash:
                nh = SARC.hash(n, self.key)
                print(f"SAHT: Fixed key {h:08X} -> {nh:08X}({self.hashes[h]})")
                self.hashes.pop(h)
                self.hashes[nh] = n
        return out
    def getName(self, key):
        return self.hashes.get(key, "")
    def __add__(self, key):
        self.hashes[SARC.hash(key, self.key)] = key
        return SAHT(self.hashes)
    def save(self, fd:IOHelper):
        self.hashes = dict(sorted(self.hashes.items(), key=lambda x:x[0]))
        foff = fd.getOffset()
        fd.writeRaw(b'SAHT',4)
        fd.writeInt(0, 32)
        fd.writeInt(self.alignment, 32)
        fd.writeInt(len(self.hashes), 32)
        for hash, fileName in self.hashes.items():
            fd.writeRawPadded(
                int.to_bytes(hash, 4, ["little","big"][fd.endian]) +
                fileName.encode("utf-8","ignore"),
                self.alignment
            )
        size = fd.getSize() - foff
        fd.setOffset(foff + 4)
        fd.writeInt(size, 32)

class SFATEntry:
    _SIZE_ = 16
    
    def __init__(self, fd:IOHelper=None, dataOff=0, mul=101):
        self.mul = mul
        self.name = 0
        self.humanName = ""
        self.strOff = 0
        self.data = b''
        if fd:
            self.name = fd.readInt(32)
            self.humanName = f"{self.name:08X}.bin"
            self.strOff = fd.readInt(32)

            dataStart = fd.readInt(32)
            dataLength = fd.readInt(32) - dataStart

            fo = fd.getOffset()
            fd.setOffset(dataStart + dataOff)
            self.data = fd.readRaw(dataLength)
            fd.setOffset(fo)
    
    def pack(self, fd:IOHelper, off, mainOff, combineDup=False, shahash:dict={}):
        if type(self.name)==str:
            fd.writeInt(SARC.hash(self.name, self.mul), 32)
        else:
            fd.writeInt(self.name, 32)
        fd.writeInt(self.strOff, 32)
        
        if combineDup:
            sh = sha256(self.data).digest()
            if sh in shahash:
                fd.writeInt(shahash[sh].fileOff, 32)
                fd.writeInt(shahash[sh].fileEnd, 32)
                return
            else:
                shahash[sh] = self
        self.fileOff = off - mainOff
        self.fileEnd = off + len(self.data) - mainOff
        fd.writeInt(self.fileOff, 32)
        fd.writeInt(self.fileEnd, 32)
        
        pad = 7

        pad = (2**pad) - 1
        dataLen = len(self.data) + pad & ~pad
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

        def __init__(self, fd:IOHelper = None, dataOff=0):
            self.unk1 = 0
            self.data = b''
            if fd:
                assert(fd.readRaw(4)==b'SFNT')
                fd.readInt(16)
                self.unk1 = fd.readInt(16)
                self.data = fd.readRaw(dataOff)
        
        def pack(self, fd:IOHelper, sfat=None):
            fd.writeRaw(b'SFNT', 4)
            fd.writeInt(self._SIZE_, 16)
            fd.writeInt(self.unk1, 16)
            fd.writeRawPadded(self.data, 4)
    
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
            s.humanName = name
            s.name = SARC.hash(name, s.mul)
            s.data = data
            s.strOff = 0
            self.nodes.append(s)

        def calcsize(self):
            return self._SIZE_ + SFATEntry._SIZE_ * len(self.nodes)

        def pack(self, fd:IOHelper, dataOff:int, combineDup=False):
            fd.writeRaw(b'SFAT', 4)
            fd.writeInt(self._SIZE_, 16)
            fd.writeInt(len(self.nodes), 16)
            fd.writeInt(self.multiplier, 32)

            off = dataOff
            self.nodes.sort()
            shaHash = dict()
            for i in self.nodes:
                i.pack(fd, off, dataOff, combineDup, shaHash)
                off = fd.getSize()

    sfnt = SFNT()
    sfat = SFAT()
    _HDR_SIZE_ = 20
    version = 256

    @staticmethod
    def hash(name, multiplier):
        if type(name) is int:
            return name
        hash = 0
        for i in name:
            hash = (hash * multiplier + ord(i)) & (2**32-1)
        return hash
    
    def hashName(self, name):
        return SARC.hash(name, self.sfat.multiplier)
    
    def hasFile(self, name):
        return self.sfat.getFile(name)!=None

    def getFile(self, name):
        vprint(f"SARC.getFile[{nametrunc(self.name)}]: {name}")
        return self.sfat.getFile(name)
    
    def setFile(self, name, data, raiseErr=False):
        if not isinstance(data, IOBase):
            if type(data) is bytes:
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
        
        vprint(f"SARC.setFile[{nametrunc(self.name)}]: {name}")
        
        if self.hasFile(name):
            self.sfat.remove(name)
        
        self.sfat.add(name, fd.read())

    def __init__(self, data=None, key=101):
        self.name = "new"
        if data:
            self.load(data)
        else:
            self.sfat = SARC.SFAT()
            self.sfnt = SARC.SFNT()

    def load(self, data):
        if not isinstance(data, IOHelper):
            self.name = "<bytes>"
            f = IOHelper(data, False)
        else:
            f = data
        
        if hasattr(f.fd, "name"): self.name = f.fd.name
        assert(f.readRaw(4)==b"SARC")
        f.readInt(16)
        f.readBOM()
        assert(f.getSize() >= f.readInt(32))
        dataOff = f.readInt(32)
        self.version = f.readInt(16)
        assert(self.version == 0x100)
        f.readRaw(2)

        self.sfat = SARC.SFAT(f, dataOff)
        self.sfnt = SARC.SFNT(f, dataOff)

    def pack(self, fd:IOHelper, combineDup=False):
        vprint(f"Packing SARC to {fd.fd.name if hasattr(fd.fd,'name') else '<bytes>'}...")
        fd.setSize(0)
        dataOff = (self._HDR_SIZE_ + self.sfat.calcsize() + self.sfnt._SIZE_ + 255) & ~255
        
        fd.writeRaw(b'SARC', 4)
        fd.writeInt(self._HDR_SIZE_, 16)
        fd.writeBOM()
        fd.writeInt(0, 32)
        fd.writeInt(dataOff, 32)
        fd.writeInt(self.version, 16)
        fd.writeInt(0, 16)

        fd.setOffset(self._HDR_SIZE_ + self.sfat.calcsize())
        self.sfnt.pack(fd, self.sfat)
        fd.setOffset(self._HDR_SIZE_)
        self.sfat.pack(fd, dataOff, combineDup)

        fd.getSize()
        fd.setOffset(8)
        fd.writeInt(fd.getSize(), 32)

    def __repr__(self) -> str:
        return f"<SARC version={self.version}, nodes={self.sfat.nodes}>"