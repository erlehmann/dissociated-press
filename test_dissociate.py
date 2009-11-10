#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as dp

s = dp.sentence("der große mann haut ein kind.")
t = dp.sentence("ein mann kotzt.")
u = dp.sentence("da ist ein kind.")
v = dp.sentence("der große baum fällt auf ein kind.")

d = dp.dictionary()

d.dissociate(s)
d.dissociate(t)
d.dissociate(u)
d.dissociate(v)

#for i in range(0,20):
#    print dict.associate()
