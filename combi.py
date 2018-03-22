#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs


with open('j1-prrg.md', 'r') as f:
    listj1 = f.read()
with open('j2-smry.md', 'r') as f:
    listj2 = f.read()
with open('j3-tril.md', 'r') as f:
    listj3 = f.read()
with open('j4-epsd.md', 'r') as f:
    listj4 = f.read()
with open('j5-medi.md', 'r') as f:
    listj5 = f.read()
with open('j6-dvlp.md', 'r') as f:
    listj6 = f.read()
with open('j7-trva.md', 'r') as f:
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
