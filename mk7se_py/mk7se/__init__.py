"""
### Mario Kart 7 Save Editor Logic

2023 CyberYoshi64
"""

import os, datetime
from ctrdash import cdss

class Logger:
    LOGFILE = "app.log"
    func = None
    file = None

    def __init__(self) -> None:
        self.func = Logger.print

    def logFile(self, *s):
        if not self.file or self.file.closed:
            if os.path.exists(self.LOGFILE): os.remove(self.LOGFILE)
            self.file = open(self.LOGFILE, "w", encoding="utf-8")
            self.file.write(f"Application log - started {datetime.datetime.isoformat(datetime.datetime.now())}\n")
        self.file.write(f"[{datetime.datetime.isoformat(datetime.datetime.now())}] ")
        for i in s:
            self.file.write(str(i))
        self.file.write("\n")
    def print(self, *s):
        print(f"[{datetime.datetime.isoformat(datetime.datetime.now())}] ", *s, sep="")
    def __call__(self, *s):
        self.func(self, *s)

class Application:
    saveData : cdss.CDSS = None
    args = None
    log = Logger()

    def __init__(self, args, isConsole=True):
        self.args = args
        if isConsole:
            self.log.func = Logger.logFile
        if self.args.input:
            try:
                self.load(self.args.input)
            except Exception as e:
                raise Exception("Initial save load failure: "+str(e))
        else:
            self.log("No save data specified; creating new")
            self.saveData = cdss.CDSS()
    
    def load(self, input):
        self.log("Try loading ", input)
        try:
            self.saveData.load(input)
        except Exception as e:
            self.log("Load failure: ",e)
            raise Exception(str(e))
        self.log("Loaded ",input," successfully!")
    
    def save(self, output):
        self.log("Try saving file as ", output)
        b = self.saveData.pack()
        if os.path.isdir(output):
            self.log("Save fail: Cannot write to folder")
            raise Exception("Cannot write to folder")
        if os.path.exists(output): os.remove(output)
        with open(output, "wb") as f:
            f.write(b)
        self.log("Saved ",output," successfully!")

    def getSave(self): return self.saveData

class Gui:
    def __init__(self, app) -> None:
        pass
    
    def run(self):
        print("Gui not implemented")
        return 1

class Console:
    pass