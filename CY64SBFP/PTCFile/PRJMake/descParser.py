#!/usr/bin/python3

def prjdscarrnot(g):
    s=""
    for i in g:
        s+="[%d]"%i
    return s

def prjdscarrfinda(a,e):
    s=[0]; g=""
    while s[0]<len(a):
        g = prjdscarrnot(s)
        if type(eval("a"+g))==list:
            if eval("a"+g+"[0]")==e: return g+"[1]"
            s.append(0)
            continue
        else:
            s.pop(); s[-1] += 1
    return None

def prjdscarrlist(a):
    s = []
    if type(a)!=list: return str(a)
    for i in a:
        s.append(i[0])
    return tuple(s)

def prjdscarrfinds(a,s):
    ens = s.split("/"); oins=""; ins=""
    for j in ens:
        ins=prjdscarrfinda(eval("a"+oins),j)
        if ins!=None: oins=oins+ins
        else: break
    return prjdscarrlist(eval("a"+oins))

def parseDescFile(f):
    a=[]; ins=""; ens=[("",-1)]; elem=[]; tmps,tmpn="",""; isMLS=False
    cidt=0; minidt=0; uci=False; tk0=""
    try: f=open(f,"rb"); fc=f.read(); f.close()
    except: return None
    fc=str(fc,"utf8").splitlines()
    for i in range(len(fc)): fc[i] = fc[i].rstrip()
    try:
        s=fc[0].split()
        if s[0]!="#CYWPTCPRJDSC" or int(s[1])>1: return None
    except: return None
    for i in range(1,len(fc)):
        s=fc[i]; idt=0; elem=[]
        while s.startswith((" ", "\t")): s=s[1:]; idt+=1
        s=s.rstrip()
        if uci: cidt=idt; uci=False
        tk=s.split(":",1)
        for j in range(len(tk)): tk[j] = tk[j].strip()
        if s=='"""':
            isMLS = not isMLS
            if isMLS: minidt=idt; tmpn=tk[0]; tmps=""
            if not isMLS:
                b = tmps.splitlines(); tmps=""
                for j in b: tmps += j[minidt:]+"\n"
                elem = [tk0, '"%s"'%tmps]
        else:
            if not isMLS and len(s):
                tk0 = tk[0]
                if len(tk)<2: raise IndexError('Stray text in descriptor file\nParsing file "%s" stopped at line %d' % (f.name, i+1))
                if i+1>=len(fc) or fc[i+1].strip()!='"""':
                    elem = [tk0]
                    if len(tk)>1: elem.append(tk[1])
            else: tmps += " "*idt + s + "\n"
        if not isMLS and (cidt>idt and not s.endswith(":")) and fc[i]!="": raise IndentationError('Misleading indentation of descriptor file\nParsing file "%s" stopped at line %d' % (f.name, i+1))
        if isMLS and s!="": minidt = min(minidt, idt)
        if not isMLS and (len(tk)==1 or tk[1]==""): uci=True
        for j in range(len(elem)):
            s=""
            if len(elem[j])>=1: s=elem[j][0]+elem[j][-1]
            if s=='""' or s=="''": elem[j]=elem[j][1:-1]
            if elem[j].isnumeric() and j: elem[j]=int(elem[j])
        if len(elem):                
            if elem[1]=="": # New category/group
                elem[1]=[]
                elem[0]=elem[0]
                while ens[-1][1]>=idt: ens.pop()
                ens.append((elem[0],idt))

            b=eval("a"); #ins=prjdscarrfinda(a,ens[-1][0])
            oins=""
            if len(ens)>1:
                for j in range(1,len(ens)):
                    ins=prjdscarrfinda(eval("a"+oins),ens[j][0])
                    if ins!=None: oins=oins+ins
                    else: break
                b=eval("a"+oins)
            b.append(elem)

        #if len(elem):print(idt, cidt, ins, ens)
    return a