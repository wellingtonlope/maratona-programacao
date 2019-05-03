# -*- coding: utf-8 -*-

c = int(input())
t = input()
m = []

for i in range(12):
    aux = []
    for j in range(12):
        aux.append(float(input()))
    m.append(aux)
    aux = []

soma = 0
for i in range(12):
    soma += m[i][c]

resultado = soma / (t == 'S' and 1 or 12)
print('%.1f' % resultado)
