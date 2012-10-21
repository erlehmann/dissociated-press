#!/usr/bin/python
# -*- coding: utf-8 -*-

#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import dissociated_press as dp
from time import sleep
from sys import argv, stderr, stdout

try:
    infile = argv[1]
    amount = int(argv[2])
except IndexError:
    stderr.write("Usage: file-dissociate-py [infile] [amount]\n")
    exit(1)

DEBUG = False
N = 2

d = dp.dictionary(debug=DEBUG)

f = open(infile,"r")
input = [x[:-1] for x in f.readlines() if x.endswith("\n")]
f.close()

for i, l in enumerate(input):
    if DEBUG:
        print l
    d.dissociate(l, N=N)
    if i%100 == 0:
        stderr.write('.')

stderr.write('\n')

try:
    while amount > 0:
        sentence = d.associate()
        if sentence not in input:
            stdout.write(sentence + '\n')
            amount = amount - 1

except KeyboardInterrupt:
    print "=== Enough! ==="
