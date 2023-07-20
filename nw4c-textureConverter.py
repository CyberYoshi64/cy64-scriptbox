#!/usr/bin/python3

import argparse, math, os, shutil
from PIL import Image

def getTempPath(createDir=False):
    if os.name == "nt":
        s = os.path.join(os.environ["TEMP"],"CyberYoshi64","NW4C_TexConv")
    else:
        s = "/tmp/CyberYoshi64/NW4C_TexConv"
    if createDir: os.makedirs(s,exist_ok=True)
    return s

def verb(*s, end="\n"):
    global args
    if not args.verbose: return
    for i in range(len(s)):
        print(str(s[i]), end="")
        print(end=(end if i==len(s)-1 else " "))
    print(end="",flush=True)

def err(rc=1, *s):
    if rc!=0:
        for i in range(len(s)):
            print(str(s[i]), end=" ")
        print(flush=True)
    p = getTempPath()
    if os.path.exists(p): shutil.rmtree(p, ignore_errors=True)
    exit(rc)

class TGAImage:
    id = None
    colors = None
    imageType = None
    origin = [0, 0]
    size = [0, 0]
    depth = 0
    fileSize_withoutDev = 0
    imgDesc = None
    image = None
    isAlpha = False
    devArea = b''

    _IMGSPEC_RTL = 1<<4
    _IMGSPEC_TTB = 1<<5
    _IMGSPEC_ALPHA = 15
    
    def __init__(self, name:str=None) -> None:
        if name.lower().endswith(".tga"):
            with open(name,"rb") as f: self.from_fd(f)
        else:
            self.load(name)

    def __str__(self) -> str:
        return "(id={}, imageType={}, size={}, devArea={})".format(self.id, self.imageType, self.size, self.devArea)

    def load(self, f):
        fn = f
        if type(f)!=str: fn = f.name
        fn = os.path.abspath(fn).encode("utf","replace")
        self.image = Image.open(f)
        self.image.load()
        self.size = list(self.image.size)
        self.isAlpha = self.image.mode.find("A")>=0
        self.depth = 24 + self.isAlpha * 8
        self.imgDesc = 8
        self.imageType = 2
        self.id = b"From file " + b"..."*(len(fn)>240) + fn[-240:]

    def colorConv(self, c, depth):
        if depth == 32: c = ((c>>16&255), (c>>8&255), (c&255), (c>>24&255))
        if depth == 16: c = ((c>>10&31)*8, (c>>5&31)*8, (c&31)*8, (c>>15&1)*255)
        if depth == 24: c = ((c>>16&255), (c>>8&255), (c&255), 255)
        if depth == 15: c = ((c>>10&31)*8, (c>>5&31)*8, (c&31)*8, 255)
        return c

    def from_fd(self, fd):
        self.fileSize_withoutDev = fd.tell()
        self.id = int.from_bytes(fd.read(1),"little")
        self.colors = True
        colors = int.from_bytes(fd.read(1),"little")
        self.imageType = int.from_bytes(fd.read(1),"little")
        isRLE = bool(self.imageType & 8)
        isPalette = (self.imageType & 7) == 1
        isGray = (self.imageType & 7) == 3

        # First entry index, Map length, Map entry size
        colors = [int.from_bytes(fd.read(2),"little"),int.from_bytes(fd.read(2),"little"),int.from_bytes(fd.read(1),"little")]

        self.origin = [int.from_bytes(fd.read(2),"little"),int.from_bytes(fd.read(2),"little")]
        self.size = [int.from_bytes(fd.read(2),"little"),int.from_bytes(fd.read(2),"little")]
        self.depth = int.from_bytes(fd.read(1),"little")
        self.imgDesc = int.from_bytes(fd.read(1),"little")

        self.isAlpha = bool(self.imgDesc & self._IMGSPEC_ALPHA)

        if self.id: self.id = fd.read(self.id)
        else: self.id = None
        
        if ((self.imageType & 7) == 0): raise Exception("TGA has no image data.")

        if isPalette:
            self.colors = []
            for i in range(colors[1]):
                self.colors.append(self.colorConv(int.from_bytes(fd.read(math.ceil(colors[2]/8)),"little"), colors[2]))
        
        if isGray:
            self.image = Image.new("L", self.size)
        else:
            self.image = Image.new("RGBA", self.size)
        bx = 0; bdx = 1; by = self.size[1]-1; bdy = -1
        if (self.imgDesc & self._IMGSPEC_RTL): bx = self.size[0]-1; bdx = -1
        if (self.imgDesc & self._IMGSPEC_TTB): by = 0; bdy = 1
        x = 0; y = 0; rc = 0; r = 0
        try:
            while y < self.size[1]:
                if isRLE:
                    rc -= 1
                    if rc < 0: # Read next RLE instruction
                        r = int.from_bytes(fd.read(1),"little")
                        if (r & 0x80): r = (r & 0x7f) # Copy next element by [r] times
                        else: rc = r; r = 0 # Read the next [r] entries and copy them
                if not isPalette:
                    c = [int.from_bytes(fd.read(math.ceil(self.depth/8)),"little")]
                    if isGray:
                        c = [c[0] * 256 // pow(2, self.depth)]
                    else:
                        c = [self.colorConv(c[0], self.depth)]
                else:
                    d = int.from_bytes(fd.read(math.ceil(self.depth/8)),"little")
                    c = []
                    if self.depth==1: # 1bit monochrome, my beloved
                                      # A byte encodes 8 pixels
                        for i in range(8):
                            c.append(self.colors[(d>>i)&1])
                    else:
                        c = [self.colors[d]]
                while r >= 0 and y < self.size[1]:
                    for i in c:
                        self.image.putpixel((bx + x * bdx, by + y * bdy), i)
                        x += 1
                        if x >= self.size[0]: x=0; y+=1
                    r -= 1
                r = 0
        except Exception as e:
            raise Exception("Failed parsing the image data: "+str(e))
        self.fileSize_withoutDev = fd.tell() - self.fileSize_withoutDev
        self.devArea = fd.read()
        if self.devArea[-18:]==b'TRUEVISION-XFILE.\0':
            self.devArea = self.devArea[:-26]
        self.image.save("out.png")
    
    def resizeImage(self, r:str):
        s = []
        if r.find(",")>=0:   s = r.split(",")[:2]
        elif r.find("-")>=0: s = r.split("-")[:2]
        elif r.find(" ")>=0: s = r.split(" ")[:2]

        if len(s)<2: raise argparse.ArgumentError(None, "Resize string invalid")
        verb("Resizing image to {} x {}.".format(s[0], s[1]))

        try:
            s[0] = int(s[0].strip(),0)
            s[1] = int(s[1].strip(),0)
        except Exception as e:
            raise argparse.ArgumentError(None, "Resize string parse fail: "+str(e))

        if s==self.size: return # Resizing with the same size

        self.image = self.image.resize(tuple(s), Image.Resampling.BICUBIC)
        self.size = s

    def processForExport(self):
        if type(self.id)==str: self.id = self.id.encode(errors="replace")[:255]
        self.depth = 24 + self.isAlpha * 8
        self.colors = []
        self.imageType = 2
        self.imgDesc = self.isAlpha * 8
        self.fileSize_withoutDev = 18 + len(self.id) + (self.size[0] * self.size[1]) * (self.depth // 8)
    
    def pil2rgb(self, f, c):
        b = f(c).ljust(4,b'\xFF')
        if not self.isAlpha: b = b[:3]
        return b

    def pil2rgb_RGB(self, c):
        b = int.to_bytes(int(c[2]),1,"little")+int.to_bytes(int(c[1]),1,"little")+int.to_bytes(int(c[0]),1,"little")+(int.to_bytes(int(c[3]),1,"little") if len(c)>3 else b'')
        return b

    def pil2rgb_L(self, c):
        return int.to_bytes(c,1,"little")*3

    def pil2rgb_LA(self, c):
        return int.to_bytes(int(c[0]),1,"little")*3+int.to_bytes(int(c[1]),1,"little")

    def export(self, name):
        verb("Exporting image",end="...")
        self.processForExport()
        with open(name, "wb") as f:
            f.truncate(0)
            f.write(int.to_bytes(len(self.id),1,"little")) # ID length
            f.write(int.to_bytes(0,1,"little"))            # Color pallette length
            f.write(int.to_bytes(self.imageType & 255,1,"little"))
            f.write(b'\0'*9)
            f.write(int.to_bytes(self.size[0], 2, "little"))
            f.write(int.to_bytes(self.size[1], 2, "little"))
            f.write(int.to_bytes(self.depth & 255,1,"little"))
            f.write(int.to_bytes(self.imgDesc & 255,1,"little"))
            f.write(self.id)
            bx = 0; bdx = 1; by = self.size[1]-1; bdy = -1
            if (self.imgDesc & self._IMGSPEC_RTL): bx = self.size[0]-1; bdx = -1
            if (self.imgDesc & self._IMGSPEC_TTB): by = 0; bdy = 1
            x = 0; y = 0; rc = 0; r = 0
            func = self.pil2rgb_RGB
            if self.image.mode == "L": func = self.pil2rgb_L
            if self.image.mode == "LA": func = self.pil2rgb_LA
            while y < self.size[1]:
                c = self.image.getpixel((bx+x*bdx, by+y*bdy))
                f.write(self.pil2rgb(func, c))
                x += 1
                if x >= self.size[0]: x=0; y+=1
            f.write(self.devArea)
        verb("done.")

class NW4C_TGAExt:
    
    _NW4CTAG_TEXFMT = "nw4c_tfm"
    _NW4CTAG_TEXDATA = "nw4c_txd"
    _NW4CTAG_TEXCREATOOL = "nw4c_gnm"
    _NW4CTAG_EOD = "nw4c_end"
    _NW4CTAG_PSH = "nw4c_psh"
    _NW4CTAG_PSH_ETCMODE = "psh_etco"
    _NW4CTAG_PSH_ETCNONALPHA = "psh_etc1"
    _NW4CTAG_PSH_ETCALPHA = "psh_etca"
    
    _ETC1ENC = (("fast"),("medium"),("slow"))
    _ETC1ENC_TEX3DS = ("low","medium","high")
    _TEXFMT = (
        ("RGBA", "RGBA8","RGB8A8","RGBA8888"),
        ("RGB", "RGB8","RGB888"),
        ("RGBA5551","RGB5A1","RGB5_A1"),
        ("RGB565","RGB_16"),
        ("RGBA4","RGBA4444","RGB4A4"),
        ("L4","I4"),
        ("L8","I8"),
        ("A4","ALPHA4"),
        ("A8","ALPHA8"),
        ("LA4","IA4"),
        ("LA8","IA8"),
        ("ETC1",False),
        ("ETC1A4","ETC1_A4",True),
        ("HILO8","RG8","RG88"),
    )
    _TEXFMT_TEX3DS = (
        "RGBA8",
        "RGB8",
        "RGBA5551",
        "RGB565",
        "RGBA4",
        "L4",
        "L8",
        "A4",
        "A8",
        "LA4",
        "LA8",
        "ETC1",
        "ETC1A4",
        "HILO8",
    )
    _TEXFMT_FILE = (
        b"Rgba8",
        b"Rgb8",
        b"Rgb5_a1",
        b"Rgb565",
        b"Rgba4",
        b"L4",
        b"L8",
        b"A4",
        b"A8",
        b"La4",
        b"La8",
        b"Etc1",
        b"Etc1_a4",
        b"Hilo8",
    )
    _NW4C_TAGNAMECNV = {
        _NW4CTAG_TEXFMT: "NW4C Texture Format",
        _NW4CTAG_TEXDATA: "NW4C Texture Data",
        _NW4CTAG_TEXCREATOOL: "Creation Tool",
        _NW4CTAG_EOD: "End of tags",
        _NW4CTAG_PSH_ETCMODE: "ETC1 Compression Type",
        _NW4CTAG_PSH_ETCNONALPHA: "ETC1 has no alpha",
        _NW4CTAG_PSH_ETCALPHA: "ETC1 has alpha",
    }
    class Tag:
        id = ""
        content = b''

        @staticmethod
        def isTag(buf, sz, doErr=False):
            if min(sz, len(buf))<12:
                if doErr: raise Exception("NW4C-Tag Error: Buffer truncated")
                return False
            p = b"abcdefghijklmnopqrstuvwxyz_-01234567889.$#/&+*^"
            n = buf[:8].rstrip(b"\0").lower()
            for i in n:
                if p.find(i)<0:
                    if doErr: raise Exception("NW4C-Tag Error: Invalid tag name: "+str(n))
                    return False
            n = int.from_bytes(buf[8:12],"little")
            if n > min(sz,0x3FFFFF):
                if doErr: raise Exception("NW4C-Tag Error: Buffer either truncated or invalid length: "+str(n))
                return False
            return True
        
        def __init__(self, id:str="", content=b'') -> None:
            self.id = str(id)[:8]
            self.content = content

        def setID(self, id):
            self.id = str(id)[:8]

        def setContent(self, content:bytes):
            self.content = content

        def to_bytes(self) -> bytes:
            b = self.id.encode("ascii","replace").ljust(8,b'\0')
            b += int.to_bytes(len(b)+4+len(self.content),4,"little")
            b += self.content
            return b
        
        def from_fd(self, fd):
            self.id = fd.read(8).decode("ascii","replace").strip()
            l = int.from_bytes(fd.read(4), "little") - 0xC
            self.content = fd.read(l)

        def from_bytes(self, buf, off=0) -> int:
            NW4C_TGAExt.Tag.isTag(buf, len(buf), True)
            self.id = buf[off:off+8].decode("ascii","replace").strip()
            l = int.from_bytes(buf[off+8:off+12], "little")
            self.content = buf[off+12:off+l]
            if len(self.content)==0: self.content = []
            return off+l
    
    isTGAforNW4C = False
    tags = []
    
    def getTags(self, buf):
        i = 0; l = []
        while i<len(buf):
            t = NW4C_TGAExt.Tag()
            try:
                i = t.from_bytes(buf, i)
            except Exception as e:
                verb("Parse Error: "+str(e))
                break
            if NW4C_TGAExt.Tag.isTag(t.content, len(t.content)):
                l2 = self.getTags(t.content)
                t.content = l2
            l.append(t)
        return l

    def load(self, tga:TGAImage):
        self.isTGAforNW4C = tga.id and \
            tga.id[:8]==b"NW4C_Tga" and \
            len(tga.id)==20
        if not self.isTGAforNW4C: raise Exception("TGA doesn't have NW4C extensions.")
        off = int.from_bytes(tga.id[16:20],"little") - tga.fileSize_withoutDev
        if off < 0: raise Exception("NW4C Extensions merge into TGA image data.")
        if off > len(tga.devArea)-12: raise Exception("TGA file is probably truncated or corrupted.")
        
        self.tags = self.getTags(tga.devArea[off:])

    def __init__(self, tga=None) -> None:
        self.isTGAforNW4C = False
        self.tags = []
        if tga==None: return
        self.load(tga)

    @staticmethod
    def nextSize(i: int):
        i -= 1; i |= i >> 1
        i |= i >> 2; i |= i >> 4
        i |= i >> 8; i |= i >> 16
        return i + 1

    @staticmethod
    def isSizeValid(size):
        if type(size)==list:
            res = True
            for i in size:
                res &= NW4C_TGAExt.isSizeValid(i)
            return res
        else:
            try: s = int(size,0)
            except: s = int(size)
            sz = [8,16,32,64,128,256,512,1024]
            try: return sz.index(s)>=0
            except: return False

    def setTag(self, id: str, data=b'', tags=None, bulk=False) -> bool:
        if tags==None: tags = self.tags
        for i in tags:
            if i.id == str:
                i.content = data
                return True
            if type(i.content)==list:
                if self.setTag(id, data, i.content, True): return True
        if not bulk:
            t = NW4C_TGAExt.Tag(id, data)
            tags.append(t)
        return False

    def getTag(self, id: str, tags=None) -> bool:
        if tags==None: tags = self.tags
        for i in tags:
            if i.id == str:
                return i.content
            if type(i.content)==list:
                d = self.getTag(id, i.content)
                if d!=None: return d
        return None

    def setTagIn(self, id: str, data=b'', tags=None) -> bool:
        if tags==None: tags = self.tags
        if type(id)==str: ids = id.split("/")
        else: ids = id+[]
        for i in tags:
            if i.id == ids[0]:
                if len(ids)==1:
                    i.content = data
                else:
                    self.setTagIn(ids[1:], data, i.content)
                return True
        
        if len(ids)==1:
            t = NW4C_TGAExt.Tag(ids[0], data)
            tags.append(t)
        return False

    def removeTag(self, id: str, tags=None) -> bool:
        if tags==None: tags = self.tags
        for i in tags:
            if i.id == str:
                tags.remove(i)
                return True
            if type(i.content)==list:
                if self.removeTag(id, i.content): return True
        return False

    def convFmtName(self, name="ETC1A4"):
        for i in range(len(self._TEXFMT)):
            for j in self._TEXFMT[i]:
                if name == j: return i
        return 12

    def getEtc1MethNameIdx(self, name=None):
        if name==None: name = "medium"
        for i in range(len(self._ETC1ENC)):
            for j in self._ETC1ENC[i]:
                if name == j: return i
        return 0

    def serialize(self, tags=None) -> bytes:
        if tags==None: tags=self.tags
        b = b''
        for i in tags:
            if type(i.content)==list:
                c = self.serialize(i.content)
            else:
                c = i.content
            b += i.id.encode("ascii","replace").ljust(8,b'\0')[:8] + int.to_bytes(12 + len(c), 4, "little") + c
        return b

    def makeNW4CTags(self, tga:TGAImage, texfmt=None, autopad=False, etc1meth=None):
        global args
        verb("Post-processing image",end="...")
        if not NW4C_TGAExt.isSizeValid(tga.size):
            if not autopad: raise Exception("Texture needs extra padding; aborting because -ap/--alert-pad specified")
            nc = Image.new("RGBA",(NW4C_TGAExt.nextSize(tga.size[0]),NW4C_TGAExt.nextSize(tga.size[1])))
            nc.paste(tga.image)
            if nc.size[0]>tga.size[0]:
                p = nc.crop((tga.size[0]-1, 0, tga.size[0], tga.size[1]))
                p = p.resize((nc.size[0]-tga.size[0]+1, tga.size[1]), Image.Resampling.NEAREST)
                nc.paste(p, (tga.size[0],0))
            if nc.size[1]>tga.size[1]:
                p = nc.crop((0,tga.size[1]-1,nc.size[0],tga.size[1]))
                p = p.resize((nc.size[0], nc.size[1]-tga.size[1]+1), Image.Resampling.NEAREST)
                nc.paste(p, (0,tga.size[1]))
        else:
            nc = tga.image.copy()
        verb("done.")
        verb("Getting image type",end="...")
        if type(texfmt)!=str: texfmt="ETC1A4" if tga.isAlpha else "ETC1"
        nwfmt = self.convFmtName(texfmt)
        verb("{} ({})".format(self._TEXFMT_TEX3DS[nwfmt],self._TEXFMT_FILE[nwfmt]))
        etc1midx = self.getEtc1MethNameIdx(etc1meth)
        etc1name = self._ETC1ENC_TEX3DS[etc1midx]
        
        verb("Creating temporary data",end="...")
        tmpPath = os.path.join(getTempPath(True),"__temp")

        nc.save(tmpPath+".png")
        self.setTag(self._NW4CTAG_TEXFMT, self._TEXFMT_FILE[nwfmt])
        execln = "tex3ds -r -o {} -z none -q {} -f {} {}".format(tmpPath+".bin", etc1name, self._TEXFMT_TEX3DS[nwfmt], tmpPath+".png")
        verb("done.")
        verb("Executing \"{}\"".format(execln),end="...")
        verb(os.system(execln))
        verb("Finalizing data",end="...")
        with open(tmpPath+".bin","rb") as f:
            f.seek(4)
            self.setTag(self._NW4CTAG_TEXDATA, f.read())
        self.isTGAforNW4C = True
        self.setTag(self._NW4CTAG_TEXCREATOOL,b'CyberYoshi64\'s NW4C TGA converter v0.1')
        self.removeTag(self._NW4CTAG_PSH)
        self.setTag(self._NW4CTAG_PSH, [])
        self.setTagIn([self._NW4CTAG_PSH, "psh_pver"], b'CyberYoshi64 was here, bro.')
        self.setTagIn([self._NW4CTAG_PSH, self._NW4CTAG_PSH_ETCALPHA if nwfmt==b'Etc1_a4' else self._NW4CTAG_PSH_ETCNONALPHA])
        self.setTagIn([self._NW4CTAG_PSH, self._NW4CTAG_PSH_ETCMODE],int.to_bytes(etc1midx,1,"little"))
        self.setTag("cy64data",[])
        self.setTagIn("cy64data/creatorN",os.environ["USERNAME"].encode("utf","replace"))
        verb("done.")

    @staticmethod
    def convName(id):
        return NW4C_TGAExt._NW4C_TAGNAMECNV.get(id, id)

def showTag(indent, tags):
    print("[")
    for i in tags:
        print("  "*indent+NW4C_TGAExt.convName(i.id))
        if type(i.content)==list:
            print("  "*indent,end="")
            showTag(indent + 1, i.content)
        else:
            print("  "*(indent+1),end="")
            if len(i.content)>80:
                print(i.content[:80].hex(),"... ({} B)".format(len(i.content)))
            else:
                print(i.content)
    print("  "*max(0,indent-1)+"]"+("" if (type(tags)!=list) else " ({})".format(len(tags))))

argprs = argparse.ArgumentParser(description="CyberYoshi64's NW4C Texture Converter")
argprs.add_argument("-v", "--verbose", action="store_true", help="Explain what is being done")
argprs.add_argument("input", action="store", help="Input file (.tga / .ctex / PIL-supported image)")
argprs.add_argument("-o", "--output", metavar="", action="store", help="Output file name")
argprs.add_argument("-t", "--type", metavar="", default="", action="store", help="Output file type (TGA / CTEX)")
argprs.add_argument("-r", "--resize", metavar="W,H", action="store", help="Resize source texture")
argprs.add_argument("-Tl", "--tag-list", action="store_true", help="Only list NW4C tags and exit")
argG1 = argprs.add_argument_group("Output Settings")
argG1.add_argument("-f", "--format", metavar="", action="store", default=None, help="Texture format")
argG1.add_argument("-ap", "--alert-pad", action="store_false", help="Abort if texture would need padding (use for optimization)")
argG1.add_argument("-ee", "--etc1enc", metavar="", default="medium", action="store", help="ETC1 compression encoding "+str(NW4C_TGAExt._ETC1ENC))
args = argprs.parse_args()

if not os.path.exists(args.input):
    err(1,"File not found:",args.input)
if not os.path.isfile(args.input):
    err(1,"Input must be a file:",args.input)
verb("Loading "+args.input,end="...")
img = TGAImage(args.input)

verb("done.")
verb("Checking for NW4C tags...",end="")
nw = NW4C_TGAExt()
try: nw.load(img)
except:
    if args.tag_list: err(1, "Error: File is not NW4C TGA.")
verb("found." if nw.isTGAforNW4C else "fail.")

if args.tag_list:
    showTag(1, nw.tags)
    err(0)

if args.output:
    if args.output.lower().strip()=="list" or args.type.lower().strip()=="list":
        print("Output types:")
        print(" - TGA (with NW4C Tags, for use with CTR_ManualEditor)")
        print(" - CTEX (XML type, for use with NWCS)")
        err(0)
    supported_types = ["tga", "ctex"]
    output_type = args.output.lower()[args.output.rfind(".")+1:]

    try: supported_types.index(output_type)
    except: output_type = args.type.lower()

    try: supported_types.index(output_type)
    except: err(2,"Invalid output type, Supported types are",supported_types)
    
    verb("Output type:",output_type)

    try:
        if args.resize: img.resizeImage(args.resize.lower())
    except Exception as e:
        err(2,"Failed resizing image: "+str(e))

    try: nw.makeNW4CTags(img, args.format, args.alert_pad, args.etc1enc)
    except Exception as e: err(2,"Failed creating NW4C data: "+str(e))


    if output_type == "tga":
        try: img.devArea = nw.serialize()
        except Exception as e: err(2,"Failed creating NW4C data: "+str(e))
        try:
            img.id = b'NW4C_Tga VerCY64'+int.to_bytes(0, 4, "little")
            img.processForExport()
            img.id = b'NW4C_Tga VerCY64'+int.to_bytes(img.fileSize_withoutDev, 4, "little")
        except Exception as e: err(2,"Failed preparing for export: "+str(e))

        try: img.export(args.output)
        except Exception as e: err(2,"Failed exporting as TGA: "+str(e))

        err(0, "Success.")
    else:
        err(254,"The output format '{}' is currently not supported.".format(output_type))
else:
    err(254,"Nothing was done.")