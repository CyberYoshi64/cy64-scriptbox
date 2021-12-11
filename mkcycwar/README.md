# mkcycwar

This script takes a folder containing BCWAV files.

Supported platforms: Linux

Modules needed: `glob`

Syntax: `python mkcycwar.py [folder] [outname]`

- `folder` — Relative path to a folder with BCWAV files inside
- `outname` — Relative path, including file name of output (without file extension)

## Warning

Although the code has some attempts to be compatibile with Windows, I cannot garantuee that this code works on Windows or macOS.

If it doesn't, you can file an issue to help me making it compatible. **Pull requests could be used, but cannot be merged, due to the way my Git setup works**

## About CYW4CTR

The `include`/`source` are an excerpt from CYW4CTR.

CYW4CTR is a side-project, starting to build up a basic framework for future 3DS homebrew of mine. It's barely functional at the moment, so I'm not uploading it on GitHub.

## Sources

- [YAMKC3DS sound class](https://github.com/PabloMK7/YAMKC_3DS/blob/main/source/Sound.cpp) by [PabloMK7](https://github.com/PabloMK7)
