# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

total = 0
maior, menor = x if x > y else y, x if x < y else y
for i in range(menor + 1 if menor % 2 == 0 else menor + 2, maior if maior % 2 == 0 else maior, 2):
    total += i

print(total)
