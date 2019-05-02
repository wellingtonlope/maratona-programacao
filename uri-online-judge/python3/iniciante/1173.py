# -*- coding: utf-8 -*-

v = int(input())
n = [v]

for i in range(1, 10):
    n.append(n[i-1]*2)

for i in range(10):
    print('N[%i] = %i' % (i, n[i]))
