#!/usr/bin/python3

import argparse, traceback, code
import mk7se

argp = argparse.ArgumentParser()
argp.add_argument("-i", "--input", help="Input save file")
# argp.add_argument("-c", "--console", action="store_true", help="Spawn as CUI instead of GUI")

args = argp.parse_args()

app = mk7se.Application(args)

try:
    #if args.console:
    #    ui = mk7se.Console(app)
    #else:
    ui = mk7se.Gui(app)

    exit(ui.run())
except Exception as e:
    app.log("An uncaught exception has occured and the application will close:\n", traceback.format_exc())
    exit(1)
