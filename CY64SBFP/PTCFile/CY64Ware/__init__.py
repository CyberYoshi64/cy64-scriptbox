#!/usr/bin/python3

from PTCFile.CY64Ware.CYWare_SB3 import *

## CY64Ware for SmileBASIC
## 2021-2022 CyberYoshi64
## 
## This module is for extensions to SmileBASIC.
## If you only want vanilla SmileBASIC types,
## please avoid this module and associated elements.

# Kill switch
CYW4PTC_ENABLE = True

#----------------------------------------------------
# Misc

CYW4PTC_KnownFmt = [
  CYW4SB3_CFD #,\ # (SB3) Compressed Font Data
  # CYW4SB3_BCFG #,\ (SB3) Binary config files
  # CYW4SB4_PCM16 #,\ # (SB4) 16bit PCM
  # CYW4SB3_CYGRP #,\ # (SB3) CYGRP (other pixel formats)
]
