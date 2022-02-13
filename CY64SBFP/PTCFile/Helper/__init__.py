#!/usr/bin/python3

import os

def mkfolders(fol:str):
  fol = "./"+fol
  g=fol[0:fol.rfind("/")]
  s=""; j=0
  while True:
    j=fol.find("/",j)+1
    if j==-1: break
    s=fol[0:j-1]
    try: os.mkdir(s)
    except OSError: pass
    if s==g: break
  try: os.mkdir(fol)
  except OSError: pass

def numClamp(x,min,max):
    if x<min: x=min
    if x>max: x=max
    return x

def hsv2rgb(h,s,v,a=255):
    r,g,b=(0,0,0)
    h = (int(h) * 10 % 3600) / 600
    s = s / 255
    if (h >= 0.0 and h < 1.0):
        r=1; g=h-int(h); b=0
    elif (h >= 1.0 and h < 2.0):
        r=1-(h-int(h)); g=1; b=0
    elif (h >= 2.0 and h < 3.0):
        r=0; g=1; b=h-int(h)
    elif (h >= 3.0 and h < 4.0):
        r=0; g=1-(h-int(h)); b=1
    elif (h >= 4.0 and h < 5.0):
        r=h-int(h); g=0; b=1
    elif (h >= 5.0):
        r=1; g=0; b=1-(h-int(h))
    if (type(a)==float): a=numClamp(a * 255, 0, 255)
    r = int(numClamp((1 - ((1 - r) * s)) * v, 0, 255))
    g = int(numClamp((1 - ((1 - g) * s)) * v, 0, 255))
    b = int(numClamp((1 - ((1 - b) * s)) * v, 0, 255))
    return (r,g,b,int(a))

def rgb2hsv(r,g,b,a=255):
    h,s = (0,0); v = max(r,g,b); l = min(r,g,b); w = v - l
    if v>0: s = numClamp((w / v) * 255, 0, 255)
    if r>=g and r>=b: h = 60 * (g-b)/w
    elif g>=r and g>=b: h = 60 * (b-r)/w + 120
    else: h = 60 * (r-g)/w + 240
    if (type(a)==float): a=numClamp(a * 255, 0, 255)
    return ((int(h * 1000)%360000)/1000,int(s)&255,int(v)&255,int(a))