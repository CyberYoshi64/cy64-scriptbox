import os
from CTGP7UpdaterApp.constants import CONSTANT as c

import CTGP7UpdaterApp.lang as lang

class CTGP7InstallationInformation:
    valid = False
    version = None
    hasPendingUpdate = False
    consideredBroken = False

    def __init__(self, folder=".") -> None:
        modFolder = os.path.join(folder, c._BASE_MOD_FOLDER_PATH)
        configFolder = os.path.join(modFolder, c._CONFIG_PATH)

        if not os.path.exists(modFolder):
            self.valid = None
            return

        if not os.path.exists(configFolder):
            self.version = False
            return
        try:
            with open(os.path.join(modFolder, *c._VERSION_FILE_PATH)) as f:
                v = f.read().encode("ascii","replace")
                if len(v)<2 or len(v)>8:
                    self.version = False
                    return
                self.version = v
            
            self.consideredBroken = os.path.exists(os.path.join(modFolder, *c._REINSTALLFLAG_PATH))
            self.hasPendingUpdate = os.path.exists(os.path.join(modFolder, *c._PENDINGUPDATE_PATH))
        except:
            self.version = False
            return
        self.valid = True

    def good(self):
        return self.valid and not self.consideredBroken
    
    def stateDescription(self):
        if self.valid == None:
            return lang.get("instVerdMissing")
        elif self.version == False:
            return lang.get("instVerdBroken")
        elif self.consideredBroken:
            return lang.get("instVerdReinstall")
        elif self.valid:
            if self.hasPendingUpdate:
                return lang.get("instVerdOKwithPend")
            return lang.get("instVerdOK")
        return lang.get("instVerdBroken")