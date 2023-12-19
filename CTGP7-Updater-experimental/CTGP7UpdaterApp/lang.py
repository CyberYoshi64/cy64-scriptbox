import os, locale, json

lang = None
data = {}

def getAppPath():
    if __name__ == "__main__":
        return (__file__[:__file__.rfind(os.sep)])
    else:
        return (__file__[:-(len(__name__)+4)])

def isNative()->bool:
    global data
    return lang[:2]=="en"

def get(key:str) -> str:
    global data
    return str(data.get(key, "[LNG:{}]".format(key)))

def tryLoadLangJson(n):
    try:
        with open(n, "r", encoding="utf-8") as f: return json.load(f)
    except:
        return None

def Initialize():
    global lang, data
    if os.name != "nt":
        locale.setlocale(locale.LC_ALL, "")
        if not lang:
            lang = locale.getlocale(locale.LC_MESSAGES)[0]
    else:
        lang = locale.getlocale()[0]
    
    path = getAppPath()
    data = {}
    flist = (
        os.path.join(path, "lang", "en.json"),
        os.path.join(path, "lang", "{}.json".format(lang)),
        os.path.join(path, "lang", "{}.json".format(lang.split("_")[0]))
    )
    for i in flist:
        tdata = tryLoadLangJson(i)
        if tdata != None:
            lang = i[i.rfind(os.sep)+1:-5]
            for k in tdata.keys():
                data[k] = tdata[k]