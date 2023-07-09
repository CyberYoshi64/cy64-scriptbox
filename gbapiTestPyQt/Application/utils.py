def strfmt(s:str, *a):
    occ = []; numpat="0123456789"
    justEv = len(s)
    while True:
        try: index = max(occ)+1
        except: index = 0
        index = s.find("%", index)
        if index<0: break
        occ.append(index)
    
    while len(occ):
        index = occ[-1]
        n = None; end = index

        if justEv != index+1:
            if s[index+1]=="[":
                end = s.find("]", index)+1
                if end > index: n = s[index+2:end-1]
            elif numpat.find(s[index+1])>=0:
                end = index + 2
                n = s[index+1]

        if not n:
            if s[index-1]=="%":
                s = s[:index]+s[index+1:]
                occ.pop(); occ.pop()
                continue
        
        if n:
            try:
                n = int(n,0)
                s = s[:index]+str(a[n])+s[end:]
            except Exception as e: print(e, index, end, n, s)
        occ.pop()
        justEv = index
    return s