#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as dp
from time import sleep

DEBUG = False
N = 2

d = dp.dictionary(debug=DEBUG)

f = open("PLOMDATA","r")
input = f.readlines()
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

        # fix line endings (why exactly does this occur ?)
        if not sentence.endswith("\n"):
            sentence = sentence + "\n"

        if sentence not in input:
            print sentence
            sleep(1)

except KeyboardInterrupt:
    print "=== Enough! ==="
