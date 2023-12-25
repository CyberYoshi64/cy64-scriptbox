VAR STC_NON%= 0,STC_STR%= 1,STC_ASC%= 2
VAR STC_U8% = 3,STC_S8% = 4,STC_U16%= 5
VAR STC_S16%= 6,STC_RSV%= 7,STC_S32%= 8
VAR STC_F64%= 9,STC_F32%=10,STC_F16%=11
VAR STC_CPL$="XSsBbHhIiFDE"

COMMON DEF StructGetTypeID(S$)RETURN INSTR(STC_CPL$,S$)END

DEF StructUnpackUnit(C%,R%,D$,DI%,AI%[],AR#[],AS$[],S%)
 VAR E%=(S%>>31)AND 1
 VAR I%,J%,L%=R%,_%,_2%,C$
 IF DI%>LEN(D$)THEN RETURN-1
 IF C%==STC_NON%THEN
  INC DI%,R%
 ELSEIF C%==STC_U8%THEN
  IF DI%+L%>LEN(D$)THEN RETURN-1
  WHILE I%<L%
   PUSH AI%,ASC(D$[DI%])
   INC DI%
  INC I%WEND
 ELSEIF C%==STC_S8%THEN
  IF DI%+L%>LEN(D$)THEN RETURN-1
  WHILE I%<L%
   PUSH AI%,(ASC(D$[DI%])<<24)>>24
   INC DI%
  INC I%WEND
 ELSEIF C%==STC_U16%THEN
  IF DI%+L%*2>LEN(D$)THEN RETURN-1
  WHILE I%<L%
   _%=ASC(D$[DI%])<<(E%*8)
   _%=_%OR ASC(D$[DI%+1])<<(!E%*8)
   PUSH AI%,_%
   INC DI%,2
  INC I%WEND
 ELSEIF C%==STC_S16%THEN
  IF DI%+L%*2>LEN(D$)THEN RETURN-1
  WHILE I%<L%
   _%=ASC(D$[DI%])<<(E%*8)
   _%=_%OR ASC(D$[DI%+1])<<(!E%*8)
   PUSH AI%,(_%<<24)>>24
   INC DI%,2
  INC I%WEND
 ELSEIF C%==STC_S32%THEN
  IF DI%+L%*4>LEN(D$)THEN RETURN-1
  WHILE I%<L%
   _%=ASC(D$[DI%])<<(E%*24)
   _%=_%OR ASC(D$[DI%+1])<<(8+E%*8)
   _%=_%OR ASC(D$[DI%+2])<<(16-E%*8)
   _%=_%OR ASC(D$[DI%+3])<<(24*!E%)
   PUSH AI%,_%
   INC DI%,4
  INC I%WEND
' ELSEIF C%==STC_RSV%THEN
'  IF DI%+L%*4>LEN(D$)THEN RETURN-1
'  WHILE I%<L%
'   _%=ASC(D$[DI%])<<(E%*24)
'   _%=_%OR ASC(D$[DI%+1])<<(8+E%*8)
'   _%=_%OR ASC(D$[DI%+2])<<(16-E%*8)
'   _%=_%OR ASC(D$[DI%+3])<<(24*!E%)
'   PUSH AI%,_%
'   INC DI%,4
'  INC I%WEND
 ELSEIF C%==STC_STR%THEN
  IF DI%+L%*2>LEN(D$)THEN RETURN-1
  C$=CHR$(0)*L%
  WHILE I%<L%
   _%=ASC(D$[DI%])<<(E%*8)
   _%=_%OR ASC(D$[DI%+1])<<(!E%*8)
   C$[I%]=CHR$(_%)
   INC DI%,2
  INC I%WEND
  PUSH AS$,C$+""
 ELSEIF C%==STC_ASC%THEN
  IF DI%+L%>LEN(D$)THEN RETURN-1
  C$=CHR$(0)*L%
  WHILE I%<L%
   C$[I%]=D$[DI%]+""
   INC DI%
  INC I%WEND
  PUSH AS$,C$+""
 ELSEIF C%==STC_F64%THEN
  IF DI%+L%*8>LEN(D$)THEN RETURN-1
  WHILE I%<L%
   _%=ASC(D$[DI%])<<(E%*24)
   _%=_%OR ASC(D$[DI%+1])<<(8+E%*8)
   _%=_%OR ASC(D$[DI%+2])<<(16-E%*8)
   _%=_%OR ASC(D$[DI%+3])<<(24*!E%)
   _2%=ASC(D$[DI%+4])<<(E%*24)
   _2%=_2%OR ASC(D$[DI%+5])<<(8+E%*8)
   _2%=_2%OR ASC(D$[DI%+6])<<(16-E%*8)
   _2%=_2%OR ASC(D$[DI%+7])<<(24*!E%)
   IF!E%THEN SWAP _%,_2%
   PUSH AR#,Raw2Float%(_%,_2%)
   INC DI%,8
  INC I%WEND
 ELSEIF C%==STC_F32%THEN
  IF DI%+L%*4>LEN(D$)THEN RETURN-1
  WHILE I%<L%
   _%=ASC(D$[DI%])<<(E%*24)
   _%=_%OR ASC(D$[DI%+1])<<(8+E%*8)
   _%=_%OR ASC(D$[DI%+2])<<(16-E%*8)
   _%=_%OR ASC(D$[DI%+3])<<(24*!E%)
   PUSH AR#,Raw2Float%(_%,0)
   INC DI%,4
  INC I%WEND
 ELSEIF C%==STC_F16%THEN
  IF DI%+L%*2>LEN(D$)THEN RETURN-1
  WHILE I%<L%
   _%=ASC(D$[DI%])<<(E%*8)
   _%=_%OR ASC(D$[DI%+1])<<(!E%*8)
   PUSH AR#,Raw2Float%(_%<<16,0)
   INC DI%,2
  INC I%WEND
 ENDIF
 RETURN DI%
END

COMMON DEF StructPackUnit(C%,R%,D,DI%,S%)
 VAR E%=(S%>>31)AND 1
 VAR I%,J%,L%=R%,_%,_2%,C$
 IF C%==STC_NON%THEN
  RETURN CHR$(0)*R%
 ELSEIF C%==STC_U8%THEN
  IF R%THEN
  IF DI%+L%>LEN(D)THEN RETURN""
  WHILE I%<L%
   INC C$,CHR$(D[DI%+I%]AND 255)
  INC I%WEND
  ELSE INC C$,CHR$(D AND 255)
  ENDIF
  RETURN C$
 ELSEIF C%==STC_S8%THEN
  IF R%THEN
  IF DI%+L%>LEN(D)THEN RETURN""
  WHILE I%<L%
   INC C$,CHR$(D[DI%+I%]AND 255)
  INC I%WEND
  ELSE INC C$,CHR$(D AND 255)
  ENDIF
  RETURN C$
 ELSEIF C%==STC_U16%THEN
  IF R%THEN
  IF DI%+L%>LEN(D)THEN RETURN""
  WHILE I%<L%
   INC C$,CHR$((D[DI%+I%]>>(8* E%))AND 255)
   INC C$,CHR$((D[DI%+I%]>>(8*!E%))AND 255)
  INC I%WEND
  ELSE
   INC C$,CHR$((D>>(8* E%))AND 255)
   INC C$,CHR$((D>>(8*!E%))AND 255)
  ENDIF
  RETURN C$
 ELSEIF C%==STC_S16%THEN
  IF R%THEN
  IF DI%+L%>LEN(D)THEN RETURN""
  WHILE I%<L%
   INC C$,CHR$((D[DI%+I%]>>(8* E%))AND 255)
   INC C$,CHR$((D[DI%+I%]>>(8*!E%))AND 255)
  INC I%WEND
  ELSE
   INC C$,CHR$((D>>(8* E%))AND 255)
   INC C$,CHR$((D>>(8*!E%))AND 255)
  ENDIF
  RETURN C$
 ELSEIF C%==STC_S32%THEN
  IF R%THEN
  IF DI%+L%>LEN(D)THEN RETURN""
  WHILE I%<L%
   INC C$,CHR$((D[DI%+I%]>>(24*E%))AND 255)
   INC C$,CHR$((D[DI%+I%]>>(8+8*E%))AND 255)
   INC C$,CHR$((D[DI%+I%]>>(16-8*E%))AND 255)
   INC C$,CHR$((D[DI%+I%]>>(24*!E%))AND 255)
  INC I%WEND
  ELSE
   INC C$,CHR$((D>>(24*E%))AND 255)
   INC C$,CHR$((D>>(8+8*E%))AND 255)
   INC C$,CHR$((D>>(16-8*E%))AND 255)
   INC C$,CHR$((D>>(24*!E%))AND 255)
  ENDIF
  RETURN C$
' ELSEIF C%==STC_RSV%THEN
'  WHILE I%<L%
'   INC C$,CHR$((D[I%]>>(24*E%))AND 255)
'   INC C$,CHR$((D[I%]>>(8+8*E%))AND 255)
'   INC C$,CHR$((D[I%]>>(16-8*E%))AND 255)
'   INC C$,CHR$((D[I%]>>(24*!E%))AND 255)
'  INC I%WEND
'  RETURN C$
 ELSEIF C%==STC_STR%THEN
  L%=MIN(R%,LEN(D))
  IF DI%+L%>LEN(D)THEN RETURN""
  WHILE I%<L%
   INC C$,CHR$((ASC(D[I%])>>(8* E%))AND 255)
   INC C$,CHR$((ASC(D[I%])>>(8*!E%))AND 255)
  INC I%WEND
  RETURN C$+CHR$(0)*MAX(0,R%*2-LEN(C$))
 ELSEIF C%==STC_ASC%THEN
  RETURN D+CHR$(0)*MAX(0,R%-LEN(D))
 ELSEIF C%==STC_F64%THEN
  IF R%THEN
  IF DI%+L%>LEN(D)THEN RETURN""
  WHILE I%<L%
   Float2Raw D[DI%+I%] OUT _%,_2%
   IF!E%THEN SWAP _%,_2%
   INC C$,CHR$((_%>>(24*E%))AND 255)
   INC C$,CHR$((_%>>(8+8*E%))AND 255)
   INC C$,CHR$((_%>>(16-8*E%))AND 255)
   INC C$,CHR$((_%>>(24*!E%))AND 255)
   INC C$,CHR$((_2%>>(24*E%))AND 255)
   INC C$,CHR$((_2%>>(8+8*E%))AND 255)
   INC C$,CHR$((_2%>>(16-8*E%))AND 255)
   INC C$,CHR$((_2%>>(24*!E%))AND 255)
  INC I%WEND
  ELSE
   Float2Raw D OUT _%,_2%
   IF!E%THEN SWAP _%,_2%
   INC C$,CHR$((_%>>(24*E%))AND 255)
   INC C$,CHR$((_%>>(8+8*E%))AND 255)
   INC C$,CHR$((_%>>(16-8*E%))AND 255)
   INC C$,CHR$((_%>>(24*!E%))AND 255)
   INC C$,CHR$((_2%>>(24*E%))AND 255)
   INC C$,CHR$((_2%>>(8+8*E%))AND 255)
   INC C$,CHR$((_2%>>(16-8*E%))AND 255)
   INC C$,CHR$((_2%>>(24*!E%))AND 255)
  ENDIF
  RETURN C$
 ELSEIF C%==STC_F32%THEN
  IF R%THEN
  IF DI%+L%>LEN(D)THEN RETURN""
  WHILE I%<L%
   Float2Raw D[DI%+I%] OUT _%,
   INC C$,CHR$((_%>>(24*E%))AND 255)
   INC C$,CHR$((_%>>(8+8*E%))AND 255)
   INC C$,CHR$((_%>>(16-8*E%))AND 255)
   INC C$,CHR$((_%>>(24*!E%))AND 255)
  INC I%WEND
  ELSE
   Float2Raw D OUT _%,
   INC C$,CHR$((_%>>(24*E%))AND 255)
   INC C$,CHR$((_%>>(8+8*E%))AND 255)
   INC C$,CHR$((_%>>(16-8*E%))AND 255)
   INC C$,CHR$((_%>>(24*!E%))AND 255)
  ENDIF
  RETURN C$
 ELSEIF C%==STC_F16%THEN
  IF R%THEN
  IF DI%+L%>LEN(D)THEN RETURN""
  WHILE I%<L%
   Float2Raw D[DI%+I%] OUT _%,:_%=_%>>16
   INC C$,CHR$((_%>>(8* E%))AND 255)
   INC C$,CHR$((_%>>(8*!E%))AND 255)
  INC I%WEND
  ELSE
   Float2Raw D OUT _%,:_%=_%>>16
   INC C$,CHR$((_%>>(8* E%))AND 255)
   INC C$,CHR$((_%>>(8*!E%))AND 255)
  ENDIF
  RETURN C$
 ENDIF
 RETURN""
END
COMMON DEF StructParse F$ OUT E%[],S%,A%[],N%
 A%=ARRAY1%(0)E%=ARRAY1%(0)N%=0S%=0
 VAR I%,L%=LEN(F$),C$,U$,M$,M%
 WHILE I%<L%
  C$=F$[I%]U$=C$
  IF C$<=" "THEN INC I%CONTINUE
  IF C$>="a"&&C$<="z"THEN U$=CHR$(ASC(C$)-32)
  IF!I%THEN
   IF C$=="<"THEN
    S%=0<<31
    INC I%CONTINUE
   ELSEIF C$==">"THEN
    S%=1<<31
    INC I%CONTINUE
   ENDIF
  ENDIF
  IF C$>="0"&&C$<="9"THEN
   INC M$,C$
  ELSE
   IF M$!=""THEN M%=VAL(M$)ELSE M%=1
   IF!M%THEN INC I%CONTINUE
   IF C$=="S"THEN
    PUSH A%,M%:INC N%,M%*2
    PUSH E%,STC_STR%
   ELSEIF C$=="s"THEN
    PUSH A%,M%:INC N%,M%
    PUSH E%,STC_ASC%
   ELSEIF C$=="B"THEN
    PUSH A%,M%:INC N%,M%
    PUSH E%,STC_U8%
   ELSEIF C$=="b"THEN
    PUSH A%,M%:INC N%,M%
    PUSH E%,STC_S8%
   ELSEIF C$=="H"THEN
    PUSH A%,M%:INC N%,M%*2
    PUSH E%,STC_U16%
   ELSEIF C$=="h"THEN
    PUSH A%,M%:INC N%,M%*2
    PUSH E%,STC_S16%
   'ELSEIF C$=="I"THEN
   ' PUSH A%,M%:INC N%,M%*4
   ELSEIF U$=="I"THEN
    PUSH A%,M%:INC N%,M%*4
    PUSH E%,STC_S32%
   ELSEIF U$=="D"THEN
    PUSH A%,M%:INC N%,M%*8
    PUSH E%,STC_F64%
   ELSEIF U$=="F"THEN
    PUSH A%,M%:INC N%,M%*4
    PUSH E%,STC_F32%
   ELSEIF U$=="E"THEN
    PUSH A%,M%:INC N%,M%*2
    PUSH E%,STC_F16%
   ELSEIF U$=="X"THEN
    PUSH A%,M%:INC N%,M%
    PUSH E%,STC_NON%
   ENDIF
   M$=""
  ENDIF
 INC I%WEND
 RETURN E$
END

COMMON DEF StructUnpack F$,D$,AI%,AR#,AS$
 VAR I%,L%,E%[0],S%,A%[0],N%,DI%
 StructParse F$ OUT E%,S%,A%,N%:L%=LEN(E%)
 WHILE I%<L%
  DI%=StructUnpackUnit(E%[I%],A%[I%],D$,DI%,AI%,AR#,AS$,S%)
  IF DI%<0THEN RETURN
 INC I%WEND
END

COMMON DEF StructPack(F$,AI%,AR#,AS$)
 VAR D$,I%,L%,E%[0],S%,A%[0],N%
 VAR II%,RI%,SI%
 StructParse F$ OUT E%,S%,A%,N%:L%=LEN(E%)
 WHILE I%<L%
  IF E%[I%]>=STC_U8%&&E%[I%]<=STC_S32%THEN
   INC D$,StructPackUnit(E%[I%],A%[I%],AI%,II%,S%)INC II%,A%[I%]
  ELSEIF  E%[I%]>=STC_F64%&&E%[I%]<=STC_F16%THEN
   INC D$,StructPackUnit(E%[I%],A%[I%],AR#,RI%,S%)INC RI%,A%[I%]
  ELSEIF  E%[I%]>=STC_STR%&&E%[I%]<=STC_ASC%THEN
   INC D$,StructPackUnit(E%[I%],A%[I%],AS$[SI%],0,S%)INC SI%
  ELSE
   INC D$,StructPackUnit(E%[I%],A%[I%],0,0,S%)
  ENDIF
 INC I%WEND
 RETURN D$
END
