# -*- coding: utf-8 -*-

for i in range(int(input())):
    x, y = map(int, input().split())
    soma = 0
    for i in range(x if x % 2 == 1 else x+1, x+(y*2), 2):
        soma += i
    print(soma)
