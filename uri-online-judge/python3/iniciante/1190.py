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
leitura = 11
for i in range(1, 11):
    for j in range(7, 12):
        if leitura <= j:
            total += 1
            soma += m[i][j]
    if i < 5:
        leitura -= 1
    if i > 5:
        leitura += 1

resultado = soma / (t == 'S' and 1 or total)
print('%.1f' % resultado)
