# -*- coding: utf-8 -*-

l = int(input())
t = input()
m = []

for i in range(12):
    aux = []
    for j in range(12):
        aux.append(float(input()))
    m.append(aux)
    aux = []

resultado = sum(m[l]) / (t == 'S' and 1 or 12)
print('%.1f' % resultado)
