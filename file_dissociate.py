#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as dp
from time import sleep

DEBUG = False
N = 2

d = dp.dictionary(debug=DEBUG)
f = open("PLOMDATA","r")
input = f.readlines()

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

f.close()
