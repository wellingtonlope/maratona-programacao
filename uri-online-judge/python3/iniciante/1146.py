# -*- coding: utf-8 -*-

while True:
    x = int(input())
    if x == 0:
        break

    [print(i, end=' ') if i != x else print(i) for i in range(1, x + 1)]
