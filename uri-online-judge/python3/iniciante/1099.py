# -*- coding: utf-8 -*-

for i in range(int(input())):
    x, y = map(int, input().split())
    maior = x if x > y else y
    menor = x if x < y else y
    total = 0
    for i in range(menor + 1 if menor % 2 == 0 else menor + 2, maior, 2):
        total += i
    print(total)
