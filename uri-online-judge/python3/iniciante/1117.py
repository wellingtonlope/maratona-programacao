# -*- coding: utf-8 -*-

notas = []
while True:
    nota = float(input())
    if 0 > nota or nota > 10:
        print('nota invalida')
        continue

    notas.append(nota)

    if len(notas) == 2:
        print('media = %.2f' % (sum(notas) / 2))
        break
