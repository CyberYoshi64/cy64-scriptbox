import os, io, enum

from struct import pack, unpack_from, calcsize

class CYCFGTypes(enum.Enum):
  Raw = 0
  String = 1
  Int32 = 2
  Double = 3

class CYCFGTypeCnv:
  @staticmethod
  def mkRawData(data):
    if type(data)==float: return pack("d", data)
    if type(data)==int: return pack("I", (data & (2**32-1)))
    if type(data)==str: return data.encode("utf-8","ignore")+chr(0)
    return data
  
  @staticmethod
  def mkStringData(data):
    if type(data)==float: return str(data)
    if type(data)==int: return str(data)
    if type(data)==str: return data
    return data.decode("utf-8","ignore").rstrip('\0')
  
  @staticmethod
  def mkIntData(data):
    if type(data)==float: return int(data) & (2**32-1)
    if type(data)==int: return data
    if type(data)==str: return int(data, 0)
    return int.from_bytes(data, "little", signed=True)
  
  @staticmethod
  def mkFloatData(data):
    if type(data)==float: return data
    if type(data)==int: return float(data)
    if type(data)==str: return float(data)
    
    if len(data)<=2: return unpack_from("e", data)[0]
    if len(data)<=4: return unpack_from("f", data)[0]
    if len(data)<=8: return unpack_from("d", data)[0]
  
  @staticmethod
  def mkRawKey(keys, key, data):
    if key in keys:
      del keys[key]
    keys[key] = [CYCFGTypes.Raw, CYCFGTypeCnv.mkRawData(data)]

  @staticmethod
  def mkStringKey(keys, key, data):
    if key in keys:
      del keys[key]
    keys[key] = [CYCFGTypes.String, CYCFGTypeCnv.mkStringData(data)]

  @staticmethod
  def mkIntKey(keys, key, data):
    if key in keys:
      del keys[key]
    keys[key] = [CYCFGTypes.Int32, CYCFGTypeCnv.mkIntData(data)]

  @staticmethod
  def mkFloatKey(keys, key, data):
    if key in keys:
      del keys[key]
    keys[key] = [CYCFGTypes.Double, CYCFGTypeCnv.mkFloatData(data)]

  @staticmethod
  def mkKey(keys, key, type, data):
    if   type == CYCFGTypes.Raw:    CYCFGTypeCnv.mkRawKey(keys, key, data)
    elif type == CYCFGTypes.String: CYCFGTypeCnv.mkStringKey(keys, key, data)
    elif type == CYCFGTypes.Int32:  CYCFGTypeCnv.mkIntKey(keys, key, data)
    elif type == CYCFGTypes.Double: CYCFGTypeCnv.mkFloatKey(keys, key, data)

  @staticmethod
  def compileKey(type, data):
    if   type == CYCFGTypes.Raw:    return data
    elif type == CYCFGTypes.String: return data.encode("utf-8","replace")+bytes((0,))
    elif type == CYCFGTypes.Int32:  return pack("I", (data & (2**32-1)))
    elif type == CYCFGTypes.Double: return pack("d", data)
    return b""

class CYCFG__V1:
  __STRUCT__ = "32s 4i"
  __ENTRY_STC__ = "2H I"
  
  def __init__(self, main, off, fd):
    self.name, dataOff, *self.reserved = \
      unpack_from(self.__STRUCT__, fd.read(calcsize(self.__STRUCT__)))
    
    self.name = self.name.strip(b'\0').decode("utf-8","ignore")
    keyCount = main.keys
    main.keys = {}
    
    dataOff -= off
    
    tbOff = fd.tell()
    for i in range(keyCount):
      nameLen, dataType, dataSize = \
        unpack_from(self.__ENTRY_STC__, fd.read(calcsize(self.__ENTRY_STC__)))
      tbOff = fd.tell()
      fd.seek(dataOff)
      keyName, keyRaw = unpack_from(f"{nameLen}s {dataSize}s", fd.read(nameLen + dataSize))
      CYCFGTypeCnv.mkKey(
        main.keys, keyName.strip(b'\0').decode("utf-8","ignore"), CYCFGTypes(dataType), keyRaw
      )
      dataOff = fd.tell()
      fd.seek(tbOff)
  def compile(self, fd, main):
  
    dataOff = fd.tell() + calcsize(self.__STRUCT__) + calcsize(self.__ENTRY_STC__) * len(main.keys)
  
    fd.write(pack(
      self.__STRUCT__, self.name.encode("utf-8","replace"),
      dataOff,
      *self.reserved
    ))
    
    tbOff = fd.tell()
    for i in main.keys:
      fd.seek(tbOff)
      keyName = i.encode("utf-8","replace")+bytes((0,))
      data = CYCFGTypeCnv.compileKey(*main.keys[i])
      fd.write(pack(
        self.__ENTRY_STC__, len(keyName), main.keys[i][0].value, len(data)
      ))
      tbOff = fd.tell()
      fd.seek(dataOff)
      fd.write(keyName)
      fd.write(data)
      dataOff = fd.tell()
    
  def __repr__(self): return str(self)
  def __str__(self): return f"<CYCFG__V1 name='{self.name}', reserved={self.reserved}>"

class CYCFG:
  __HEADSTRUCT__ = "8s 2H I"
  
  closed = True
  keys = 0
  
  def __init__(self, data=None):
    self.keys = 0
    self.cfg = None
    self.closed = True
    self.version = 0
    
    if data: self.decompile(data)
  
  def compile(self, out=None):
    fd = io.BytesIO()
    
    fd.write(pack(
      self.__HEADSTRUCT__, b'CY64%CFG', 0, 0, 0
    ))
    
    if hasattr(self.cfg,"compile"):
      self.cfg.compile(fd, self)
    
    s = fd.tell()
    fd.seek(0)
    fd.write(pack(
      self.__HEADSTRUCT__, b'CY64%CFG', self.version, len(self.keys), s
    ))
    
    if not isinstance(out, io.IOBase):
      b = fd.getvalue()
      fd.close()
      return b
    else:
      fd.seek(0)
      while True:
        b = fd.read(32768)
        if not len(b): break
        out.write(b)
      fd.close()

  def decompile(self, data):
    if type(data)==str:
      fd = open(data, "rb")
      self.closed = False
    elif type(data)==tuple:
      fd = open(data[0], "rb")
      fd.seek(data[1])
      self.closed = False
    elif isinstance(data, io.IOBase):
      fd = data
    else:
      fd = io.BytesIO(data)
    
    try:
      self.offset = fd.tell()
      mgc, self.version, self.keys, self.size = unpack_from(
        self.__HEADSTRUCT__, fd.read(calcsize(self.__HEADSTRUCT__))
      )
      assert(mgc == b"CY64%CFG")
      if self.version == 1:
        self.cfg = CYCFG__V1(
          self, fd.tell(), io.BytesIO(fd.read(self.size - calcsize(self.__HEADSTRUCT__)))
        )
      else:
        raise Exception("Unknown CYCFG version: "+str(self.version))
    except Exception as e:
      if not self.closed: fd.close()
      raise Exception(e)
    else:
      if not self.closed: fd.close()
  def __repr__(self): return str(self)
  def __str__(self): return f"<CYCFG version={self.version}, cfg={self.cfg}, keys=Keys[{len(self.keys)}]>"
  def print(self):
  	print("CYCFG {")
  	print(f" - Version    : {self.version}")
  	print(f" - Misc. data : {self.cfg}")
  	print(f" - Keys       : [")
  	for i in self.keys:
  	  print(f"     '{i.ljust(32)}': [{self.keys[i][0].name.ljust(6)}, {self.keys[i][1]}]")
  	print(f"   ]")
  	print("}")
