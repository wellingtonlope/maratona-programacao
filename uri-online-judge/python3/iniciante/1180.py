# -*- coding: utf-8 -*-

n = int(input())
x = list(map(int, input().split()))

menor = min(x)
posicao = x.index(menor)

print('Menor valor: ' + str(menor))
print('Posicao: ' + str(posicao))
