# -*- coding: utf-8 -*-

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        for j in range(n):
            numero = '%i' % (abs(i - j) + 1)
            if j == 0:
                print('%s%s' % (' ' * (3 - len(numero)), numero), end='')
            else:
                print('%s%s' % (' ' * (4 - len(numero)), numero), end='')
        print()
    print()
