# -*- coding: utf-8 -*-

valores = sorted(list(map(float, input().split())), reverse=True)

if valores[0] >= valores[1] + valores[2]:
    print('NAO FORMA TRIANGULO')
else:
    if valores[0] ** 2 == valores[1] ** 2 + valores[2] ** 2:
        print('TRIANGULO RETANGULO')
    if valores[0] ** 2 > valores[1] ** 2 + valores[2] ** 2:
        print('TRIANGULO OBTUSANGULO')
    if valores[0] ** 2 < valores[1] ** 2 + valores[2] ** 2:
        print('TRIANGULO ACUTANGULO')
    if valores[0] == valores[1] and valores[0] == valores[2]:
        print('TRIANGULO EQUILATERO')
    if valores[0] == valores[1] and valores[0] != valores[2] or valores[0] == valores[2] and valores[0] != valores[1] or valores[1] == valores[2] and valores[1] != valores[0]:
        print('TRIANGULO ISOSCELES')
