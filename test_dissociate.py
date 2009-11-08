#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as d

s = d.sentence("Der behandschuhte Mann haut ein Kind.")
t = d.sentence("Der Mann kotzt.")
u = d.sentence("Ein Kind kotzt.")
v = d.sentence("")

dict = d.dictionary()

s.dissociate(dict)
t.dissociate(dict)
u.dissociate(dict)
v.dissociate(dict)

for i in range(0,20):
    print dict.associate()
