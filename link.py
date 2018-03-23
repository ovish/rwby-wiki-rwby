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

# 人力リンクで作業してある<ref link />をのける
listTidy = re.split('<ref.+?\/>', strJpn)
tidyJpn = ''.join(listTidy)

listJpn = re.split('\[\^\d+\]', tidyJpn)
listLink = re.findall('<ref.*?>.+?<\/ref>', strLink)

listSource = [
    str(lineJpn) + str(lineLink)
    for (lineJpn, lineLink)
    in zip_longest(listJpn, listLink)
    ]

with open('jpnSource.txt', 'w') as f:
        f.write(''.join(listSource))
