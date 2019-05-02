# -*- coding: utf-8 -*-

n = int(input())
anterior = 1
atual = 0

for i in range(n):
    if i != n -1:
        print(atual, end=' ')
        aux = atual
        atual += anterior
        anterior = aux
    else:
        print(atual)
