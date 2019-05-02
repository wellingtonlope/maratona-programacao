# -*- coding: utf-8 -*-

linha = list(map(int, input().split()))

a = linha[0]
n = linha[len(linha) - 1]

total = 0
for i in range(a, a + n):
    total += i

print(total)
