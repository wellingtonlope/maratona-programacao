# -*- coding: utf-8 -*-

while True:
    x, y = map(int, input().split())
    if x == y:
        break
    print('Crescente') if x < y else print('Decrescente')
