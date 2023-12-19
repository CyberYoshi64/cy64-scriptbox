#!/usr/bin/python3

import cy64_cycfg

c = cy64_cycfg.common.CYCFG("sample_v1.cycfg")
c.print()
with open("test.cycfg", "wb") as f:
  c.compile(f)