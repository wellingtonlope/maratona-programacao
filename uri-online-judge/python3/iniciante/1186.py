# -*- coding: utf-8 -*-

t = input()
m = []

for i in range(12):
    aux = []
    for j in range(12):
        aux.append(float(input()))
    m.append(aux)
    aux = []

soma = 0
total = 0
coluna = 11
for i in range(12):
    for j in range(12):
        if j > coluna:
            total += 1
            soma += m[i][j]
    coluna -= 1

resultado = soma / (t == 'S' and 1 or total)
print('%.1f' % resultado)
