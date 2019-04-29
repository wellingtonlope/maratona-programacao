# -*- coding: utf-8 -*-

valores = []

[valores.append(int(input())) for i in range(int(input()))]

i = 0
o = 0

for x in valores:
    if x >= 10 and x <= 20:
        i += 1
    else:
        o += 1

print('%i in' % i)
print('%i out' % o)
