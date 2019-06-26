# -*- coding: utf-8 -*-

while True:
    try:
        n = int(input())

        for i in range(n):
            for j in range(n):
                numero = 3
                if i == j:
                    numero = 1
                if i + j == n - 1:
                    numero = 2
                print(numero, end='')
            print()
    except EOFError:
        break
