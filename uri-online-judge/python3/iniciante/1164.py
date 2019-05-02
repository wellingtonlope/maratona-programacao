# -*- coding: utf-8 -*-

for i in range(int(input())):
    x = int(input())
    soma = 0
    for j in range(1, x):
        soma += j if x % j == 0 else 0

    if x == soma:
        print('%i eh perfeito' % x)
    else:
        print('%i nao eh perfeito' % x)
