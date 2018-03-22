#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs
from itertools import zip_longest

with open('jpnCombi.md', 'r') as f:
    strJpn = f.read()
with open('source.md', 'r') as f:
    strLink = f.read()

listJpn = re.split('\[\^\d+\]', strJpn)
listLink = re.findall('<ref.*?>.+?<\/ref>', strLink)

listSource = [
    str(lineJpn) + str(lineLink)
    for (lineJpn, lineLink)
    in zip_longest(listJpn, listLink)
    ]

with open('jpnSource.txt', 'w') as f:
        f.write(''.join(listSource))
