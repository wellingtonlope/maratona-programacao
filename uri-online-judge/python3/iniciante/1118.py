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

        alternativa = 0
        while 1 != alternativa != 2:
            alternativa = int(input('novo calculo (1-sim 2-nao)\n'))
        if alternativa == 2:
            break

        notas = []
