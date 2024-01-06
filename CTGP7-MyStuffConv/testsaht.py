#!/usr/bin/python3

from ctgp7tools.misc.sarc import SAHT, SARC
from ctgp7tools.misc.csarData import CWAV_OFF
from ctgp7tools.misc.gameEnum import *
from ioHelper import IOHelper

try:
    with open("HashTable.saht","rb") as f:
        s = SAHT(IOHelper(f))
        if not s.verify("remove"):
            print("!! HashTable has bad keys!")
except Exception as e:
    print("HashTable.saht not found; grab it from EFE or CTR Studio.")
    print("Error: "+str(e))
    exit(1)

if True:
    for i in CWAV_OFF.keys():
        for j in range(len(CWAV_OFF[i])):
            if type(i) is int:
                s.getAddHash(f"SND_{i:02}_{j:02}.bcwav")

    s.getAddHash("SND_select.bcwav")
    s.getAddHash("SND_go.bcwav")
    s.getAddHash("config.ini")
    s.getAddHash("stdWingColor.ips")
    s.getAddHash("driver.bcmdl")
    s.getAddHash("driver_lod.bcmdl")
    s.getAddHash("emblem.bcmdl")
    s.getAddHash("emblem_lod.bcmdl")
    s.getAddHash("thankyou_anim.bcmdl")
    s.getAddHash("select.bclim")
    s.getAddHash("rankrace.bclim")
    s.getAddHash("rankmenu.bclim")
    s.getAddHash("maprace.bclim")

    for i in BodyNames:
        s.getAddHash(f"body_{i}.bcmdl")
        s.getAddHash(f"body_{i}_lod.bcmdl")
        s.getAddHash(f"body_{i}_shadow.bcmdl")

    for i in TireNames:
        s.getAddHash(f"tire_{i}.bcmdl")
        s.getAddHash(f"tire_{i}_lod.bcmdl")
        s.getAddHash(f"tire_{i}_shadow.bcmdl")

    for i in WingNames:
        s.getAddHash(f"wing_{i}.bcmdl")
        s.getAddHash(f"wing_{i}_lod.bcmdl")

    for i in ScrewNames:
        s.getAddHash(f"screw_{i}.bcmdl")
        s.getAddHash(f"screw_{i}_lod.bcmdl")

for k,n in s.hashes.items():
    print(f"{k:08X} {n}")

with open("HashTable2.saht","wb") as f:
    s.save(IOHelper(f))