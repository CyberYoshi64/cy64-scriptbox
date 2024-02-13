class CONSTANT:
    VERSION_CAT_STABLE, VERSION_CAT_RC, \
    VERSION_CAT_BETA, VERSION_CAT_ALPHA, \
    VERSION_CAT_DEV = range(5)
    VERSION_NUMBER = {
        "major": 1,
        "minor": 1,
        "micro": 3,
        "category": VERSION_CAT_DEV
    }
    _BASE_MOD_FOLDER_PATH = "CTGP-7"
    _BASE_MOD_NAME = "CTGP-7"
    _BASE_URL_DYN_LINK = "https://ctgp7.page.link/baseCDNURL"
    _INSTALLER_VERSION = "installerver"
    _INSTALLER_FILE_DIFF = "installinfo.txt"
    _UPDATER_CHGLOG_FILE = "changeloglist"
    _UPDATER_FILE_URL = "fileListPrefix.txt"
    _INTCHECK_HASH_URL = "hashes.txt" # Unofficial
    _FILES_LOCATION = "data"
    _FILES_LOCATION_CITRA = "dataCitra"
    _LATEST_VER_LOCATION = "latestver"
    _DL_ATTEMPT_TOTALCNT = 30

    _CONFIG_PATH = "config"

    _SAVEBAK_MOD_PATH = [_BASE_MOD_FOLDER_PATH, "savefs"]
    _SAVEBAK_BAK_PATH = "CTGP-7savebak"

    _VERSION_FILE_PATH = [_CONFIG_PATH, "version.bin"]
    _PENDINGUPDATE_PATH = [_CONFIG_PATH, "pendingUpdate.bin"]
    _ISCITRAFLAG_PATH = [_CONFIG_PATH, "citra.flag"]
    _REINSTALLFLAG_PATH = [_CONFIG_PATH, "forceInstall.flag"]
    _PATCHFLAG_PATH = [_CONFIG_PATH, "forcePatch.flag"]
    _EXPECTEDVER_PATH = [_CONFIG_PATH, "expectedVer.bin"]
    _SLACK_FREE_SPACE = 33554432 # 32 MiB

    _APPPACKAGE_CIA_PATH = [_BASE_MOD_FOLDER_PATH, "cia", "CTGP-7.cia"]
    _APPPACKAGE_CIA_TEMP = [_BASE_MOD_FOLDER_PATH, "cia", "tooInstall.cia"]
    _APPPACKAGE_HBL_PATH_SRC = [_BASE_MOD_FOLDER_PATH, "cia", "CTGP-7.3dsx"]
    _APPPACKAGE_HBL_PATH_DEST = ["3ds", "CTGP-7.3dsx"]
    _APPPACKAGE_HBL_TEMP = [_BASE_MOD_FOLDER_PATH, "cia", "tooInstall.3dsx"]

    _MODE_INSTALL, _MODE_UPDATE, _MODE_INTCHECK, \
    _MODE_DOWNLOAD = range(4)