#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import codecs

with open('combi.md', 'r') as f:
    strJpn = f.read()
with open('source.md', 'r') as f:
    strLink = f.read()

listJpn = re.split('\[\^\d+\]', strJpn)
listLink = re.findall('<ref.*?>.+?<\/ref>', strLink)

listSource = [
    lineJpn + lineLink
    for i, (lineJpn, lineLink)
    in enumerate(zip(listJpn, listLink))
    ]
print(listLink)
