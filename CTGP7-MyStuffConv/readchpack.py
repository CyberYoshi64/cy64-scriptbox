#!/usr/bin/python3

import ctgp7tools
from ctgp7tools.misc.gameEnum import *
import os, sys
from ioHelper import IOHelper
from glob import glob

import shutil

shutil.rmtree("temp", True)
c = ctgp7tools.mystuff.character.v2.Character(
    sys.argv[1]
)

print(c.cfgkeys)
print(c.driver)
print(c.karts)
print(c.stdWingColor)
print(c.thankyou_anim)
print(c.sounds)

for i in c.sounds:
    with open("out-"+i,"wb") as f:
        f.write(c.sarc.getFile(i).data)