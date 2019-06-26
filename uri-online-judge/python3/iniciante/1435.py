# -*- coding: utf-8 -*-

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        for j in range(n):
            menor = min(i + 1, j + 1, n - i, n - j)
            if j == 0 or menor >= 10:
                print('  %i' % menor, end='')
            else:
                print('   %i' % menor, end='')
        print()
    print()
