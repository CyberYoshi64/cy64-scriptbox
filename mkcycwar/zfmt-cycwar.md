# CYCWAR

## Construction

```text
Header
Sound descriptor 1
Sound descriptor 2
.
.
.
Sound descriptor n
Raw BCWAV data
```

## Header

Offset | Type/Size    | Name    | Description
------:|:------------:|:--------|:------------------------
 0x00  | String (8)   | fmagic  | Magic `CY64CWAR`
 0x08  | Uint16LE (2) | fver    | Format version
 0x0A  | Uint16LE (2) | cwavcnt | Amount of BCWAV embedded
 0x0C  | Uint32LE (4) | cwavoff | Offset to raw BCWAV data

## Sound descriptor

**Warning!** These offsets shown are relative.

Offset |   Type/Size   | Name  | Description
------:|:-------------:|:------|:----------------------------
 0     | String (*n*)  | sname | Sound name (+ NUL-terminator)
 *n*+0 | Uint32LE (4)  | ssize | BCWAV data length
 *n*+4 | Uint8 (1)     | sflag | Sound flags

### sflag

Bit | Part name | Description
----|-----------|-------------------
 0  | cwavloopf | Sound loop flag
1-7 | cwavsplyc | Sound play maximum

## Raw BCWAV data

This section contains BCWAV file contents back-to-back.

## Quirks

- If `cwavoff` is greater than sound descriptor n's sflag, plus 1 byte, or beyond the end of the CWAV data, you can inject any data. This could be used for comments or other miscellaneous data.
