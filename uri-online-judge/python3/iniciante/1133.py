# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

maior = x if x > y else y
menor = x if x < y else y

[print(i) if i % 5 == 3 or i % 5 == 2 else 0 for i in range(menor + 1, maior)]
