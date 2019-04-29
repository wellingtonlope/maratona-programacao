# -*- coding: utf-8 -*-

maior = 0
posicao = 0

for i in range(100):
    x = int(input())
    if maior < x:
        maior = x
        posicao = i + 1

print(maior)
print(posicao)
