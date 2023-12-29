#!/usr/bin/python3

import ctgp7tools
from ctgp7tools.misc.gameEnum import *
import os, sys
from ioHelper import IOHelper
from glob import glob

root = "/data/0/data/Citra/sdmc/CTGP-7"
prgwd = os.path.dirname(__file__)

import shutil

shutil.rmtree("temp", True)

assets = os.path.join(
    prgwd, "assets/romfs"
)
myst = os.path.join(root, "MyStuff", "Characters")

for i in glob("*/", root_dir=myst):
    c = ctgp7tools.mystuff.character.v1.Character(
        os.path.join(myst, i)
    )

    print(i)

    ctgp7tools.mystuff.character.v2.convertV1(
        src = c,
        bcsp = assets,
        outName=f"{i[:-1]}.chpack"
    )