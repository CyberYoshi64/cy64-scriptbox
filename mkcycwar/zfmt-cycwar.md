# CYCWAR

## Construction

```text
Header
Sound descriptor 1
Sound descriptor 2
...
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

`cwavcnt` is designed to take 1 to 65535 BCWAVs (including the 3DS's own memory limitations).

`cwavoff` must have an offset, bigger than the end of the header and the sound descriptors's offsets. `mkcycwar.py` will set the offset automatically, however, if messed with, will result in invalidating almost all of the sound entries.

## Sound descriptor

**Warning!** These offsets shown are relative.

Offset |   Type/Size   | Name  | Description
------:|:-------------:|:------|:----------------------------
 0     | String (*n*)  | sname | Sound name (+ NUL-terminator)
 *n*+0 | Uint32LE (4)  | ssize | BCWAV data length
 *n*+4 | Uint8 (1)     | sflag | Sound flags

`sname` can theoratically be as long as you want, however, a seperate limitation is included in the CYCWAR loader routine. ***This is not finalised, therefore it's not statically defined, how many characters are actually allowed, before being truncated on-the-fly upon loading.***

### sflag - Further detail

Bit | Part name | Description
----|-----------|-------------------
 0  | cwavloopf | Sound loop flag
1-7 | cwavsplyc | Sound play maximum

`cwavsplyc` dictates, how many instances of a sound can play at once.
The raw value is obtained by arithmetically shifting `sflag` once to the right, like so:

```cpp
u8 CYCWAR::get_cwavsplyc(u8 sflag){
    return (sflag >> 2) & 127; // Some weird value can return, if not using "u8" or "unsigned char".
}
```

## Raw BCWAV data

This section contains BCWAV file contents back-to-back.

Do not attempt injecting other data between entries, as that will invalidate all entries coming after said injection.

## Quirks

- If `cwavoff` is greater than the last sound's `sflag` + 1 byte, you can inject any data between this gap. This could be used for comments or other miscellaneous data in a future revision of this format.
