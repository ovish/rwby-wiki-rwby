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

#コメント消去
listJpnC = re.split('<\!--.+-->', strLink)
# 人力リンクで作業してある<ref link />をのける
listTidy = re.split('<ref.+?\/>', ''.join(listJpnC))


listLink = re.findall('<ref.*?>.+?<\/ref>', ''.join(listTidy))
listJpn = re.split('\[\^\d+\]', strJpn)

listSource = [
    str(lineJpn) + str(lineLink)
    for (lineJpn, lineLink)
    in zip_longest(listJpn, listLink)
    ]

#コメント消去
listSourceC = re.split('<\!--.+-->', ''.join(listSource))

with open('jpnSource.md', 'w') as f:
        f.write(''.join(listSourceC))
