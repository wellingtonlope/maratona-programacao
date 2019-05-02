# -*- coding: utf-8 -*-

while True:
    n = int(input())
    if n == 0:
        break
    soma = 0
    for i in range(n if n % 2 == 0 else n + 1, n + (2 * 5), 2):
        soma += i
    print(soma)
