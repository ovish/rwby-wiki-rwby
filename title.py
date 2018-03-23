#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# link.pyにぶっこんだ方が作業楽

import re
import sys
import os
import codecs
from itertools import zip_longest

with open('jpnCombi.md', 'r') as f:
    strJpn = f.read()

# こいつを#と###と##のぶんやるハッシュ4から
# pythonの正規表現かっこつけると抜き出せる？
listJpn = re.split('### .*', strJpn)
listTitle = re.findall('### (.+)', strJpn)
listHash3 = [
    str(lineJpn) + '====' + str(lineTitle) + '===='
    for (lineJpn, lineTitle)
    in zip_longest(listJpn, listTitle)
    ]
hash3 = ''.join(listHash3)

listJpn = re.split('## .*', hash3)
listTitle = re.findall('## (.+)', hash3)
listHash2 = [
    str(lineJpn) + '===' + str(lineTitle) + '==='
    for (lineJpn, lineTitle)
    in zip_longest(listJpn, listTitle)
    ]
hash2 = ''.join(listHash2)

listJpn = re.split('# .*', hash2)
listTitle = re.findall('# (.+)', hash2)
listHash1 = [
    str(lineJpn) + '==' + str(lineTitle) + '=='
    for (lineJpn, lineTitle)
    in zip_longest(listJpn, listTitle)
    ]
hash1 = ''.join(listHash1)

# 元のファイル上書きする
with open('jpnCombi.md', 'w') as f:
        f.write(hash1)
