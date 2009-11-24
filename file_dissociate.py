#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as dp
from time import sleep
from sys import argv

if len(argv) == 1:
    infile = "PLOMDATA"
else:
    infile = argv[1]

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
        print i

try:
    while 1:
        sentence = d.associate()
        if sentence not in input:
            print sentence
            sleep(1)

except KeyboardInterrupt:
    print "=== Enough! ==="
