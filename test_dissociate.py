#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as dp

d = dp.dictionary()

d.dissociate("der große mann haut ein kind.")
d.dissociate("ein mann kotzt.")
d.dissociate("da ist ein kind.")
d.dissociate("der große baum fällt auf ein kind.")

for i in range(0,20):
    print d.associate()
