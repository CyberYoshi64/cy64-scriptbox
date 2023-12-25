#!/usr/bin/python3

import cy64_cycfg

print("""
CYCFG parse test v1.0
---------------------""")

print("\n --- Plain file 'sample_v1.cycfg'\n")
c = cy64_cycfg.common.CYCFG("sample_v1.cycfg")
c.print()
with open("test.cycfg", "wb") as f:
    c.compile(f)

print("\n --- Embedded in SmileBASIC 3 file 'BOSSAVE.bin'\n")
with open("BOSSAVE2.bin", "rb") as fin:
    fin.seek(0x6C)
    c = cy64_cycfg.common.CYCFG(fin)
    c.print()
    with open("test2.cycfg", "wb") as f:
        c.compile(f)

