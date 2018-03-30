#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs

#j[num]は直訳、c[num]は翻訳
with open('c1-prrg.md', 'r') as f:
    listj1 = f.read()
with open('c2-smry.md', 'r') as f:
    listj2 = f.read()
with open('c3-tril.md', 'r') as f:
    listj3 = f.read()
with open('c4-epsd.md', 'r') as f:
    listj4 = f.read()
with open('c5-medi.md', 'r') as f:
    listj5 = f.read()
with open('c6-dvlp.md', 'r') as f:
    listj6 = f.read()
with open('c7-trva.md', 'r') as f:
    listj7 = f.read()

listCombi = str(
    listj1
    + "\n"
    + listj2
    + "\n"
    + listj3
    + "\n"
    + listj4
    + "\n"
    + listj5
    + "\n"
    + listj6
    + "\n"
    + listj7
    )

with open('jpnCombi.md', 'w') as f:
    f.write(listCombi)
