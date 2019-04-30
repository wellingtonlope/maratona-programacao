# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

maior = x if x > y else y
menor = x if x < y else y
total = 0

for i in range(menor, maior + 1):
    total += i if i % 13 != 0 else 0

print(total)
