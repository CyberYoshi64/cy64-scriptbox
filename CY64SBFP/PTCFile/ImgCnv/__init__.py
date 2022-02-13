#!/usr/bin/python3
import cv2, numpy, struct, random

CNV_ARGB8, CNV_BGR8, CNV_RGBA5551, CNV_LA4, CNV_L8, CNV_RGB332,\
CNV_RGBA3221, CNV_HSV844, CNV_HSVA7441, CNV_A8, CNV_LA8, CNV_RGBX2 =\
    range(12)

def getFmtByteCnt(f):
    try: return (4,3,2,1,1,1,1,2,2,1,2,1)[f]
    except: return 0

# For ImgCnv.convertImage()
def packRGBA(t,ofm):
    if type(t)!=tuple or len(t)!=4: return None
    if min(t)<0 or max(t)>255: return None # Is the color in Uint8 bounds?
    if ofm == CNV_ARGB8:
        return struct.pack("<BBBB",t[3],t[0],t[1],t[2])
    if ofm == CNV_BGR8:
        return struct.pack("<BBB",t[2],t[1],t[0])
    if ofm == CNV_RGBA5551:
        return struct.pack("<H",
        bool(t[3])*1 | int(t[0]/8)<<11 | int(t[1]/8)<<6 | int(t[2]/8)<<1)

# For ImgCnv.convertImage()
def getRGBAFromBuf(ifm, buf, idx):
    r,g,b,a = 0,0,0,0; pxl = getFmtByteCnt(ifm)
    if type(buf)!=bytearray: return None
    # if (idx % pxl)!=0: return None # Might not be feasible with file-ceptions
    if idx < 0 or idx+pxl > len(buf): return None
    if ifm == CNV_ARGB8:
        a,r,g,b = struct.unpack("<BBBB",buf[idx:idx+4])
    if ifm == CNV_BGR8:
        b,g,r = struct.unpack("<BBB",buf[idx:idx+3])
    if ifm == CNV_RGBA5551:
        im = struct.unpack("<H",buf[idx:idx+2])[0]
        r,g,b,a = \
        ((im>>11)&31) * 8, ((im>>6)&31) * 8, \
        ((im>>1)&31) * 8, (im&1)*255
    return (r,g,b,a)

def getImageFromFile(f): # Output is ARGB8-encoded data (ready for SB4 GRP/META)
    img = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
    w, h = len(img[0]), len(img)
    buf = bytearray(w * h * 4)
    for i in range(w):
        for j in range(h):
            for k in range(4):
                buf[(i + j * w) * 4 + k] = img[j][i][3-k]
    return [CNV_ARGB8, w, h, buf]

def saveImageToFile(buf, f) -> bool:
    if type(buf)!=list or len(buf)!=4: return False
    if type(buf[0])!=int or type(buf[1])!=int or type(buf[2])!=int or type(buf[3])!=bytearray: return False
    nbuf = buf
    
    # If input buffer does not have ARGB8 data, convert it
    if buf[0] != CNV_ARGB8: nbuf = convertImage(buf, CNV_ARGB8, False)
    if nbuf == None: return False
    w, h = buf[1:3]
    
    ih = [] # Unpack into array for numpy array for cv2.imwrite
    for i in range(h):
        iw = []
        for j in range(w):
            ic=[]
            for k in range(4):
                ic.append(nbuf[3][(j + i * w) * 4 + 3 - k])
            iw.append(ic)
        ih.append(iw)
    return cv2.imwrite(f, numpy.array(ih))

def cvtImg_applySpcFltr(t, x, y, fid):
    if type(t)!=tuple or len(t)!=4: return None
    if min(t)<0 or max(t)>255: return None
    r,g,b,a = t
    if fid&1: # Simple dithering through randomizing a small amount
        r += random.randint(-2,5)
        g += random.randint(-2,5)
        b += random.randint(-2,5)
    if fid&2: # Bayer-like filtering (?! at least I'm trying, lmao)
        r += -2 + (7 * ((x+y) % 2))
        g += -2 + (2 * ((x+y+2) % 3))
        b += -2 + (7 * ((x+y+1) % 2))
    if fid&4: # Magenta -> Transparent
        if r>244 and g<7 and b>244: r,g,b,a = (0,0,0,0)
    if fid&8: # Grayscale
        m=r*.35+b*.2+g*.45
        r,g,b = m,m,m
    r=int(min(255,max(0,r)))
    g=int(min(255,max(0,g)))
    b=int(min(255,max(0,b)))
    a=int(min(255,max(0,a)))
    return (r,g,b,a)
def convertImage(buf, outfmt, sp=0):
    if type(buf)!=list or len(buf)!=4: return None
    if type(buf[0])!=int or type(buf[1])!=int or type(buf[2])!=int or type(buf[3])!=bytearray: return None
    infmt, w, h = buf[:3]
    nbuf = bytearray()
    stp = getFmtByteCnt(infmt)
    for i in range(0, w*h*stp, stp):
        t=getRGBAFromBuf(infmt,buf[3],i)
        t=cvtImg_applySpcFltr(t, (i/stp %w), int(i/stp/w), sp)
        b = packRGBA(t,outfmt)
        if b==None: return None
        nbuf += b
    return [outfmt, w, h, nbuf]