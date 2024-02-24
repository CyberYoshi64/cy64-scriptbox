#!/usr/bin/python3

import struct
import argparse
import os

args = argparse.ArgumentParser()
args.add_argument("-f","--file",nargs=1,required=True,help="Config file")
args.add_argument("-b","--block",nargs=1,required=True,help="Config block ID")
args.add_argument("-x","--extract",nargs=1,required=False,help="Export block to file")
args.add_argument("-i","--inject",nargs=1,required=False,help="Import data from file")
arg = args.parse_args()

try:
    argblock = int(arg.block[0], 16)
except:
    argblock = int(arg.block[0])

with open(arg.file[0], "r+b") as f:
    block_count,data_offset = struct.unpack('HH', f.read(4))

    entries=[]; keys = []
    for i in range(block_count):
        entries.append(struct.unpack('IIHH', f.read(12)))
        keys.append(entries[-1][0])

    index = keys.index(argblock)
    blockDataOff = 4 + index * 12 + 4

    blockID, dataOff, size, perm = entries[index]

    if size > 4: blockDataOff = dataOff

    if arg.extract:
        with open(arg.extract[0], "wb") as g:
            f.seek(blockDataOff, os.SEEK_SET)
            g.write(f.read(size))
    elif arg.inject:
        with open(arg.inject[0], "rb") as g:
            f.seek(blockDataOff, os.SEEK_SET)
            f.write(g.read(size).ljust(size, b'\0'))
