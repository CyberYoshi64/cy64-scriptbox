"""
## CTGP-7 Tools
"""

VERBOSE = False

if VERBOSE:
    def vprint(*s, **kwd):
        print(*s, **kwd)
else:
    def vprint(*s, **kwd):
        pass

from . import mystuff, misc