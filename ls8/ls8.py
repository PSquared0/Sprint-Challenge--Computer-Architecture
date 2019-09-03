#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

if len(sys.argv) != 2:
   print(sys.stderr)
   sys.exit(1)

else:
   cpu = CPU()
   cpu.load()
   cpu.run() 

cpu = CPU()

cpu.load()
cpu.run()