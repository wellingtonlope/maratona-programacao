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
leitura = 0
for i in range(5):
    for j in range(12):
        if leitura < j < 11 - leitura:
            total += 1
            soma += m[i][j]
    leitura += 1

resultado = soma / (t == 'S' and 1 or total)
print('%.1f' % resultado)
