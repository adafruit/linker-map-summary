# MIT License
#
# Copyright (c) 2016 Scott Shawcroft for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import print_function

import sys

size_by_source = {}
with open(sys.argv[1]) as f:
  memory_map_started = False
  current_section = None
  for line in f:
    if memory_map_started:
      if True or line.startswith((".", " .")):
        pieces = line.split()
        if line.startswith("."):
          current_section = pieces[0]
        elif len(pieces) >= 3 and current_section in [".rodata", ".text"] and "=" not in pieces and "before" not in pieces:
          if pieces[0] == "*fill*":
            source = pieces[0]
            size = int(pieces[-1], 16)
          else:
            source = pieces[-1]
            size = int(pieces[-2], 16)
          if source not in size_by_source:
            size_by_source[source] = 0
          size_by_source[source] += size
    elif line.strip() == "Linker script and memory map":
      memory_map_started = True

sources = size_by_source.keys()
sources.sort(key=lambda x: size_by_source[x])
for source in sources:
  print(source, size_by_source[source])
