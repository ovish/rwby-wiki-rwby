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
listTidy = re.split('<ref.+?\/>', strLink)
tidyLink = ''.join(listTidy)

listLink = re.findall('<ref.*?>.+?<\/ref>', tidyLink)
listJpn = re.split('\[\^\d+\]', strJpn)

listSourceWithC = [
    str(lineJpn) + str(lineLink)
    for (lineJpn, lineLink)
    in zip_longest(listJpn, listLink)
    ]
strSourceWithC = ''.join(listSourceWithC)

#コメント消去
listSource = re.split('<\!--.+-->', strSourceWithC)

with open('jpnSource.md', 'w') as f:
        f.write(''.join(listSource))
