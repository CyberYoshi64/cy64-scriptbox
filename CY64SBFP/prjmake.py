#!/usr/bin/python3

import PTCFile.PRJMake.descParser as dscParse
import os, sys, glob
from sys import argv

prgerr=0
PRGMODE_LIST, PRGMODE_VERIFY, PRGMODE_BUILD = ("list","verify","build")

prgavailmode = (PRGMODE_LIST, PRGMODE_VERIFY, PRGMODE_BUILD)

#try:
if len(argv)<2: raise IndexError("Not enough arguments, need at least 1 argument")
prgmode = argv[1]
try: prgavailmode.index(prgmode)
except: raise ValueError("Unknown command: %s"%prgmode)

if prgmode == PRGMODE_LIST:
    proj = glob.glob("*/*.rsf")
    print(proj)
if prgmode == PRGMODE_VERIFY:
    print(dscParse.parseDescFile("NewProject1/project.txt"))
    #pass
if prgmode == PRGMODE_BUILD:
    pass

#except:
#    errtype, errvalue, errtrace = sys.exc_info()
#    if errtype!=SystemExit:
#        #print("\n An error has occured while running the script.\n")
#        #traceback.print_exception(errtype, errvalue, errtrace)
#        print("\nAn exception occured (%s):\n %s\n" % (str(errtype).split("'")[1],str(errvalue)))
#        prgerr=True

exit(prgerr)