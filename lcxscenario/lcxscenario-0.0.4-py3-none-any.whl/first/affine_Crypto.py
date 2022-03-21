#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： moddemod
# datetime： 2019/12/27 下午9:50
# ide： PyCharm

# y = 17x-8 flag{szzyfimhyzd}

import gmpy2
s = 'szzyfimhyzd'
r = gmpy2.invert(17, 26)

s1 = ''
for i in s:
    s1 += chr(r * (ord(i) - ord('a') + 8) % 26 + ord('a'))
print('flag{' + s1 + '}')

