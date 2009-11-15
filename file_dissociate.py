#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as dp
from time import sleep

d = dp.dictionary()
f = open("TESTDATA","r")
input = f.readlines()

for l in input:
    print l
    d.dissociate(l)

try:
    while 1:
        sentence = d.associate()

        if sentence not in input:
            print sentence
        else:
            print "FAIL:", sentence

        sleep(1)

except KeyboardInterrupt:
    print "=== Enough! ==="

f.close()
