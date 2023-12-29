VAR CYCFGT_RAW%=0,CYCFGT_STR%=1
VAR CYCFGT_INT%=2,CYCFGT_F64%=3
VAR CYCFGSTC$="8sHHI16S4I"
VAR CYCFGSGN$="CY64%CFG",CYCFGVER%=1
VAR CYCFGERR%,CYCFG_CRCISFATAL%=1
DIM CYCFGP$[0],CYCFGI%[0],_CYCFGI%,_CYCFGT$
DIM CYCFGN$[0],CYCFGT%[0],CYCFGV$[0]

COMMON DEF CYCFG_Err%()RETURN CYCFGERR%END
COMMON DEF CYCFG_Err$()RETURN CYCFG__Err$(CYCFGERR%)END
COMMON DEF CYCFG__Err$(ERRINDEX%)
 IF ERRINDEX%>0 THEN RETURN CYFS_STRIM$(MID$("Failed to read from file                      Truncated data                                Bad signature or incompatible version         Unknown config version                        Out-of-bounds pointer                         Insufficient resources                        Already loaded                                Bad CRC                                                                                                                                   ",(ERRINDEX%-1)*46,46))ELSEIF!ERRINDEX%THEN RETURN"OK"ELSE RETURN"Unknown error"
END

COMMON DEF CYCFG_CRCErrCode()RETURN 8:END
COMMON DEF CYCFG_IsCRCErrCode()RETURN CYCFGERR%==CYCFG_CRCErrCode()END

COMMON DEF CYCFG_SetCRCFatal T%
 CYCFG_CRCISFATAL%=""==T%<3||T%
END

COMMON DEF CYCFG_GetCRCFatal()
 RETURN CYCFG_CRCISFATAL%
END

COMMON DEF CYCFG_New(P$)VAR R%=-6,S$=LEFT$(UCAPS$(P$),16)
 IF _CYCFGI%>&H7FFF0000THEN RETURN-6
 IF FIND(CYCFGP$,S$)<0THEN PUSH CYCFGP$,S$INC _CYCFGI%PUSH CYCFGI%,_CYCFGI%R%=_CYCFGI%
 RETURN R%
END

COMMON DEF CYCFG_Close ID%
 VAR P$,PI%=FIND(CYCFGI%,ID%)
 IF PI%<0THEN RETURN
 P$=CYCFGP$[PI%]+":"
 REMOVE CYCFGP$,PI%
 REMOVE CYCFGI%,PI%
 VAR I%,L%=LEN(CYCFGN$)
 CYCFG_Tick
 WHILE I%<L%
  IF LEFT$(CYCFGN$[I%],LEN(P$))==P$THEN
   REMOVE CYCFGN$,I%
   REMOVE CYCFGV$,I%
   REMOVE CYCFGT%,I%
   DEC L%CONTINUE
  ENDIF
 INC I%WEND
END

COMMON DEF CYCFG_Load(P$,D$)
 VAR K%,O%,R%,I%
 VAR K$,N%,_0%,_1%,_2%,_3%,_0$,_1$
 VAR STCA$[0],STCA%[0],IDX%[0]
 IF D$==0!=3THEN RETURN-9337
 IF LEN(D$)>32THEN
  _CYCFGT$=D$
 ELSE
  IF!CHKFILE2("TXT:"+D$)THEN R%=-1GOTO@END
  _CYCFGT$=LOAD("TXT:"+D$,0)
 ENDIF
 N%=LEN(_CYCFGT$)-4
 IF CRC32_O%(LEFT$(_CYCFGT$,N%))!=ASC2INT_LE%(RIGHT$(_CYCFGT$,4),4)THEN
  IF CYCFG_CRCISFATAL%THEN R%=-8GOTO@END ELSE ?"CYCFG_Load(): Bad CRC - Config untrusted"
 ENDIF
 CYCFG_Tick
 StructParse CYCFGSTC$OUT,,,N%
 StructUnpack CYCFGSTC$,_CYCFGT$,STCA%,,STCA$
 IF LEN(STCA$)<2THEN R%=-2GOTO@END
 IF LEN(STCA%)<4THEN R%=-2GOTO@END
 IF STCA$[0]!=CYCFGSGN$THEN R%=-3GOTO@END
 IF STCA%[0]>CYCFGVER%THEN R%=-4GOTO@END
 IF STCA%[2]>LEN(_CYCFGT$)THEN R%=-5GOTO@END
 K%=STCA%[1]:O%=STCA%[3]
 STCA%=ARRAY1%(0)
 StructUnpack "2HI"*K%,MID$(_CYCFGT$,N%,9E8),STCA%,,
 INC N%,8*K%
 R%=CYCFG_New(P$)IF R%<1THEN GOTO@END
 
 I%=0WHILE I%<K%
  _0$=CYFS_STrim$(FromUTF8$(MID$(_CYCFGT$,O%,STCA%[I%*3+0])))
  INC O%,STCA%[I%*3+0]
  _1$=MID$(_CYCFGT$,O%,STCA%[I%*3+2])
  INC O%,STCA%[I%*3+2]
  IF STCA%[I%*3+1]==CYCFGT_STR%THEN _1$=FromUTF8$(_1$)IF _1$[LEN(_1$)-1]==CHR$(0)&&POP(_1$)THEN:
  CYCFG_Write R%,_0$,_1$,0
  CYCFGT%[LEN(CYCFGT%)-1]=STCA%[I%*3+1]
 INC I%WEND
@END
 _CYCFGT$=""CYCFGERR%=MAX(0,-R%)
 RETURN R%
END

DEF CYCFG_CnvVal(I%)
 IF I%<0||I%>=LEN(CYCFGT%)THEN RETURN"undefined"
 IF CYCFGT%[I%]==CYCFGT_RAW%THEN
  RETURN CYCFGV$[I%]
 ELSEIF CYCFGT%[I%]==CYCFGT_STR%THEN
  RETURN CYCFGV$[I%]
 ELSEIF CYCFGT%[I%]==CYCFGT_INT%THEN
  RETURN ASC2INT_LE%(CYCFGV$[I%],4)
 ELSEIF CYCFGT%[I%]==CYCFGT_F64%THEN
  RETURN Raw2Float%(ASC2INT_LE%(MID$(CYCFGV$[I%],4,4),4),ASC2INT_LE%(MID$(CYCFGV$[I%],0,4),4))
 ENDIF
 RETURN"[UNKNOWN]"
END

DEF CYCFG_CnvVal%(I%)
 IF I%<0||I%>=LEN(CYCFGT%)THEN RETURN"undefined"
 RETURN CYCFG_CnvImmediate(CYCFGT%[I%],CYCFGV$[I%])
END

COMMON DEF CYCFG_CnvImmediate(T%,V$)
 IF T%==CYCFGT_RAW%THEN
  RETURN HEXDMPT$(FORMAT$("[%D]“%S”",LEN(V$),V$))
 ELSEIF T%==CYCFGT_STR%THEN
  RETURN QU$+V$+QU$
 ELSEIF T%==CYCFGT_INT%THEN
  RETURN ASC2INT_LE%(V$,4)
 ELSEIF T%==CYCFGT_F64%THEN
  RETURN Raw2Float%(ASC2INT_LE%(MID$(V$,4,4),4),ASC2INT_LE%(MID$(V$,0,4),4))
 ENDIF
 RETURN"[UNKNOWN]"
END

COMMON DEF CYCFG_CnvImmediate$(T%,V$)
 IF T%==CYCFGT_RAW%THEN
  RETURN HEXDMPT$(FORMAT$("[%D]",LEN(V$))+V$)
 ELSEIF T%==CYCFGT_STR%THEN
  RETURN QU$+V$+QU$
 ELSEIF T%==CYCFGT_INT%THEN
  RETURN STR$(ASC2INT_LE%(V$,4))
 ELSEIF T%==CYCFGT_F64%THEN
  RETURN FORMAT$("%.6F",Raw2Float%(ASC2INT_LE%(MID$(V$,4,4),4),ASC2INT_LE%(MID$(V$,0,4),4)))
 ENDIF
 RETURN"[UNKNOWN]"
END

COMMON DEF CYCFG_Read(ID%,K$,D)
 VAR P$,PI%=FIND(CYCFGI%,ID%)
 IF PI%<0THEN RETURN D
 P$=CYCFGP$[PI%]+":"+UCAPS$(K$)
 VAR I%=FIND(CYCFGN$,P$)
 IF I%<0THEN RETURN D
 RETURN CYCFG_CnvVal(I%)
END

COMMON DEF CYCFG_ReadRaw ID%,K$ OUT T%,V$
 T%=-1V$=""
 VAR P$,PI%=FIND(CYCFGI%,ID%)
 IF PI%<0THEN RETURN
 P$=CYCFGP$[PI%]+":"+UCAPS$(K$)
 VAR I%=FIND(CYCFGN$,P$)
 IF I%<0THEN RETURN
 T%=CYCFGT%[I%]V$=""+CYCFGV$[I%]
END

COMMON DEF CYCFG_Write ID%,K$,V,T%
 VAR P$,PI%=FIND(CYCFGI%,ID%)
 IF PI%<0THEN RETURN
 P$=CYCFGP$[PI%]+":"+UCAPS$(K$)
 VAR I%=FIND(CYCFGN$,P$)
 IF I%<0THEN
  I%=LEN(CYCFGN$)
  PUSH CYCFGN$,P$
  PUSH CYCFGV$,""
  PUSH CYCFGT%,0
 ENDIF
 CYCFGT%[I%]=T%
 IF 0THEN
 ELSEIF T%==CYCFGT_RAW%THEN CYCFGV$[I%]=S_STR1$(V)
 ELSEIF T%==CYCFGT_STR%THEN CYCFGV$[I%]=S_STR2$(V)
 ELSEIF T%==CYCFGT_INT%THEN
  CYCFGV$[I%]=INT2ASC_LE$(S_INT(V),4)
 ELSEIF T%==CYCFGT_F64%THEN
  VAR _%,_2%
  Float2Raw S_FLOAT(V) OUT _%,_2%
  CYCFGV$[I%]=INT2ASC_LE$(_2%,4)+INT2ASC_LE$(_%,4)
 ELSE CYCFGV$[I%]=""
 ENDIF
END

COMMON DEF CYCFG_Delete ID%,K$
 VAR P$,PI%=FIND(CYCFGI%,ID%)
 IF PI%<0THEN RETURN
 P$=CYCFGP$[PI%]+":"+UCAPS$(K$)
 VAR I%=FIND(CYCFGN$,P$)
 IF I%>=0THEN
  REMOVE CYCFGN$,I%
  REMOVE CYCFGV$,I%
  REMOVE CYCFGT%,I%
 ENDIF
END

COMMON DEF CYCFG_DeleteSub ID%,K$
 VAR P$,PI%=FIND(CYCFGI%,ID%)
 IF PI%<0THEN RETURN
 P$=CYCFGP$[PI%]+":"+UCAPS$(K$)+"/"
 VAR I%,L%=LEN(CYCFGN$)
 WHILE I%<L%
  IF LEFT$(CYCFGN$[I%],LEN(P$))==P$THEN
   REMOVE CYCFGN$,I%
   REMOVE CYCFGV$,I%
   REMOVE CYCFGT%,I%
   DEC L%CONTINUE
  ENDIF
 INC I%WEND
END

COMMON DEF CYCFG_SubExists(ID%,K$)
 VAR P$,PI%=FIND(CYCFGI%,ID%)
 IF PI%<0THEN RETURN 0
 P$=CYCFGP$[PI%]+":"+UCAPS$(K$)+"/"
 VAR I%,L%=LEN(CYCFGN$)
 WHILE I%<L%
  IF LEFT$(CYCFGN$[I%],LEN(P$))==P$THEN RETURN 1
 INC I%WEND
 RETURN 0
END

COMMON DEF CYCFG_List(ID%)
 VAR P$,PI%=FIND(CYCFGI%,ID%),K$[0]
 IF PI%<0THEN RETURN K$
 P$=CYCFGP$[PI%]+":"
 VAR I%,L%=LEN(CYCFGN$)
 WHILE I%<L%
  IF LEFT$(CYCFGN$[I%],LEN(P$))==P$THEN PUSH K$,MID$(CYCFGN$[I%],LEN(P$),9E6)
 INC I%WEND
 RETURN K$
END

COMMON DEF CYCFG_DbgList ID%,V
 VAR P$,PI%=FIND(CYCFGI%,ID%)
 IF PI%<0THEN RETURN
 P$=CYCFGP$[PI%]+":"
 VAR I%,L%=LEN(CYCFGN$)
 WHILE I%<L%
  IF LEFT$(CYCFGN$[I%],LEN(P$))==P$THEN ?CYCFGT%[I%],MID$(CYCFGN$[I%],LEN(P$),9E6),CYCFG_CnvVal%(I%)WAIT V
 INC I%WEND
END

COMMON DEF CYCFG_DbgListAll V
 VAR I%,L%=LEN(CYCFGN$)
 WHILE I%<L%
  ?CYCFGT%[I%],CYCFGN$[I%],CYCFG_CnvVal(I%)WAIT V
 INC I%WEND
END

COMMON DEF CYCFG_Tick
 VAR L%=LEN(CYCFGN$),L2%=LEN(CYCFGV$),L3%=LEN(CYCFGT%)
 IF L2%<L%THEN RESIZE CYCFGN$,L2%L%=L2%
 IF L3%<L%THEN RESIZE CYCFGN$,L3%L%=L3%
 IF L2%>L%THEN RESIZE CYCFGV$,L%
 IF L3%>L%THEN RESIZE CYCFGT%,L%
 IF L%THEN SORT CYCFGN$,CYCFGT%,CYCFGV$
 L%=LEN(CYCFGI%)L2%=LEN(CYCFGP$)
 IF L2%<L%THEN RESIZE CYCFGI%,L2%L%=L2%
 IF L2%>L%THEN RESIZE CYCFGP$,L%
 IF L%THEN SORT CYCFGI%,CYCFGP$
END

COMMON DEF CYCFG_Serialize(ID%)
 VAR P$,PI%=FIND(CYCFGI%,ID%)
 VAR K%,K$,D$,N%,_0%,_1%,_2%,_3%,_0$,_1$
 VAR STCA$[0],STCA%[0],IDX%[0],I%,L%=LEN(CYCFGN$)
 IF PI%<0THEN RETURN""
 P$=CYCFGP$[PI%]+":"
 CYCFG_Tick
 WHILE I%<L%
  IF LEFT$(CYCFGN$[I%],LEN(P$))==P$THEN PUSH IDX%,I%
 INC I%WEND
 
 PUSH STCA$,CYCFGSGN$
 PUSH STCA%,CYCFGVER%
 PUSH STCA%,LEN(IDX%)
 PUSH STCA$,CYCFGP$[PI%]
 StructParse CYCFGSTC$OUT,,,N%
 I%=0L%=LEN(IDX%)WHILE I%<L%
  _0$=ToUTF8$(MID$(CYCFGN$[IDX%[I%]],LEN(P$),60))+CHR$(0)
  IF LEN(_0$)AND 3THEN INC _0$,CHR$(0)*(4-(LEN(_0$)AND 3))
  _1$=CYCFGV$[IDX%[I%]]
  IF CYCFGT%[IDX%[I%]]==CYCFGT_STR%THEN _1$=ToUTF8$(_1$)+CHR$(0)
  IF LEN(_1$)AND 3THEN INC _1$,CHR$(0)*(4-(LEN(_1$)AND 3))
  INC K$,LEFT$(INT2ASC_LE$(LEN(_0$),4),2)
  INC K$,LEFT$(INT2ASC_LE$(CYCFGT%[IDX%[I%]],4),2)
  INC K$,INT2ASC_LE$(LEN(_1$),4)
  INC D$,_0$:INC D$,_1$
 INC I%WEND
 
 IF LEN(K$)AND 15THEN INC K$,CHR$(0)*(16-(LEN(K$)AND 15))
 IF LEN(D$)AND 15THEN INC D$,CHR$(0)*(16-(LEN(D$)AND 15))
 INC D$,CHR$(0)*12
 
 PUSH STCA%,N%+LEN(K$)+LEN(D$)+4
 PUSH STCA%,N%+LEN(K$)
 PUSH STCA%,-1
 PUSH STCA%,-1
 PUSH STCA%,-1
 _CYCFGT$=StructPack(CYCFGSTC$,STCA%,,STCA$)+K$+D$
 RETURN _CYCFGT$+INT2ASC_LE$(CRC32_O%(_CYCFGT$),4)
END