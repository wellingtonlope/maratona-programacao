# -*- coding: utf-8 -*-

x = []
for i in range(10):
    x.append(int(input()))

x = list(map(lambda x: 1 if x <= 0 else x, x))

for i in range(10):
    print('X[%i] = %i' % (i, x[i]))
