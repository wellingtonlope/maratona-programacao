# -*- coding: utf-8 -*-

while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    maior = m if m > n else n
    menor = m if m < n else n

    total = 0
    for i in range(menor, maior + 1):
        print(i, end=' ')
        total += i
    print('Sum=' + str(total))
