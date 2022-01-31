#!/usr/bin/python3
import cv2, numpy, math, struct, random

CNV_ARGB8, CNV_BGR8, CNV_RGBA5551, CNV_LA4, CNV_L8, CNV_RGB332,\
CNV_RGBA3221, CNV_HSV844, CNV_HSVA7441, CNV_A8, CNV_LA8, CNV_RGBX2 =\
	range(12)

def getFmtByteCnt(f):
	try: return (4,3,2)[f]
	except: return 0

def packRGBA(t,ofm):
	if type(t)!=tuple or len(t)!=4: return None
	if min(t)<0 or max(t)>255: return None
	if ofm == CNV_ARGB8:
		return struct.pack("<BBBB",t[3],t[0],t[1],t[2])
	if ofm == CNV_BGR8:
		return struct.pack("<BBB",t[2],t[1],t[0])
	if ofm == CNV_RGBA5551:
		return struct.pack("<H",
		bool(t[3])*1 | int(t[0]/8)<<11 | int(t[1]/8)<<6 | int(t[2]/8)<<1
		)

def getRGBAFromBuf(ifm, buf, idx):
	r,g,b,a = 0,0,0,0; pxl = getFmtByteCnt(ifm)
	if type(buf)!=bytearray: return None
	# if (idx % pxl)!=0: return None
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

def getImageFromFile(f):
	img = cv2.imread(f, cv2.IMREAD_UNCHANGED)
	img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
	w, h = len(img[0]), len(img)
	buf = bytearray(w * h * 4)
	for i in range(w):
		for j in range(h):
			for k in range(4):
				buf[(i + j * w) * 4 + k] = img[j][i][3-k]
	return [CNV_ARGB8, w, h, buf]

def saveImageToFile(buf, f):
	if type(buf)!=list or len(buf)!=4: return False
	if type(buf[0])!=int or type(buf[1])!=int or type(buf[2])!=int or type(buf[3])!=bytearray: return False
	nbuf = buf
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
	if fid==1:
		r += random.randint(0,7)
		g += random.randint(0,7)
		b += random.randint(0,7)
	if fid==2:
		r += 7 * ((x+y) % 2)
		g += 4
		b += 7 * ((x+y+1) % 2)
	if fid==10:
		if r>244 and g<7 and b>244: r,g,b,a = (0,0,0,0)
	if fid==11:
		m=r*.5+b*.1+g*.4
		r,g,b = m,m,m
	return (r,g,b,a)
def convertImage(buf, outfmt, sp=0):
	if type(buf)!=list or len(buf)!=4: return None
	if type(buf[0])!=int or type(buf[1])!=int or type(buf[2])!=int or type(buf[3])!=bytearray: return None
	infmt, w, h = buf[:3]
	nbuf = bytearray()
	stp = getFmtByteCnt(infmt); j=0
	for i in range(0, w*h*stp, stp):
		t=getRGBAFromBuf(infmt,buf[3],i)
		cvtImg_applySpcFltr(t, i%w, int(i/w), sp)
		b = packRGBA(t,outfmt)
		if b==None: return None
		nbuf += b
		j+=1
	return [outfmt, w, h, nbuf]