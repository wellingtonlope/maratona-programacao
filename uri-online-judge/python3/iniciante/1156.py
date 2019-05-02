# -*- coding: utf-8 -*-

x = 1.0
y = 1.0
s = 0
while x <= 39:
    s += x / y
    x += 2
    y *= 2

print('%.2f' % s)
