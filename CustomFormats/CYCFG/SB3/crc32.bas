VAR CRC32T%[256],CRC32TI%,CRC32M%=&HEDB88320

DEF CRC32__INIT(M%)
 DIM C%,I%,J%
 VAR A%[0]A%=ARRAY1%(256)
 WHILE I%<256
  C%=I%
  J%=0WHILE J%<8
   IF C%AND 1THEN C%=M%XOR((C%>>1)AND&H7FFFFFFF)ELSE C%=(C%>>1)AND&H7FFFFFFF
  INC J%WEND
  A%[I%]=C%
 INC I%WEND
 RETURN A%
END

DEF CRC32__C%(A%,R%,B$)
 VAR I%,L%=LEN(B$)
 WHILE I%<L%
  R%=((R%>>8)AND&HFFFFFF)XOR A%[(R%XOR ASC(B$[I%]))AND 255]
 INC I%WEND
 RETURN R%
END

COMMON DEF CRC32_C%(R%,B$)
 IF!CRC32TI%THEN CRC32_INIT
 RETURN CRC32__C%(CRC32T%,R%,B$)
END

COMMON DEF CRC32_LC%(A%,R%,B$)
 IF LEN(A%)!=256THEN RETURN 0
 RETURN CRC32__C%(A%,R%,B$)
END

COMMON DEF CRC32_D%(R%)
 RETURN R%XOR-1
END

COMMON DEF CRC32_INIT
 CRC32T%=CRC32__INIT(CRC32M%)CRC32TI%=1
END

COMMON DEF CRC32_MKTBL%(MGC%)
 VAR M%IF!MGC%||""==MGC%>1THEN M%=CRC32M%ELSE M%=MGC%
 RETURN CRC32__INIT(M%)
END

COMMON DEF CRC32%(B$)
 IF!CRC32TI%THEN CRC32_INIT
 RETURN CRC32_C%(-1,B$)
END

COMMON DEF CRC32_O%(B$)
 IF!CRC32TI%THEN CRC32_INIT
 RETURN CRC32_D%(CRC32_C%(-1,B$))
END

COMMON DEF CRC32_L%(A%,B$)
 RETURN CRC32_LC%(A%,-1,B$)
END

COMMON DEF CRC32_LO%(A%,B$)
 RETURN CRC32_D%(CRC32_LC%(A%,-1,B$))
END
