# -*- coding: utf-8 -*-

a = []
for i in range(100):
    a.append(float(input()))

for i in range(100):
    if a[i] <= 10:
        print('A[%i] = %.1f' % (i, a[i]))
