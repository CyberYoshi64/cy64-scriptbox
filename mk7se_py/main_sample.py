#!/usr/bin/python3

import os, sys, io, struct
import ctr, ctrdash

with open(sys.argv[1],"rb") as fd:
	cdss = ctrdash.cdss.CDSS(fd)
	print(cdss.str())

cdss.cec_comment = "Hello there."
cdss.miiData.miiName = "ＣＹ６４ιαsοη"
cdss.miiData.miiID = 0x80001337
cdss.flagData.vr = 99999
cdss.flagData.wins = 99999
cdss.flagData.losses = 99999
cdss.flagData.cecMeets = 99999
cdss.flagData.coins = 0xFFFFFFFF # NOTE: wtf it works
cdss.flagData.tracks = 0xFFFF  # TODO: Determine bitmask
cdss.flagData.chars = 0xFFFF   # TODO: Determine bitmask
cdss.flagData.karts = 0xFFFF   # TODO: Determine bitmask
cdss.flagData.tires = 0xFFFF   # TODO: Determine bitmask
cdss.flagData.gliders = 0xFFFF # TODO: Determine bitmask

for i in range(32):
	cdss.trophy.setEntry(i, 3, 6, True) # Gold + 3 stars

with open("out.dat","wb") as fd:
	fd.write(cdss.pack())