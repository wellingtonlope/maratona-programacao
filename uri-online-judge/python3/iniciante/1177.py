# -*- coding: utf-8 -*-

n = []
t = int(input())
aux = 0
for i in range(1000):
    if aux == t:
        aux = 0
    n.append(aux)
    aux += 1

for i in range(1000):
    print('N[%i] = %i' % (i, n[i]))
