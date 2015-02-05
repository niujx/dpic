# -*- coding: utf-8 -*-
__author__ = 'yanshi'
import re

line = '"10：00——24:00",,,0,,,,0,,"8，21,70,53,343路到阳公桥站下",,,,,,"小吃快餐",,"钵钵鸡"'
for a in re.findall('(".*?")', line, re.MULTILINE):
    new = a.replace(",", "||||")
    line = line.replace(a, new)

print line
