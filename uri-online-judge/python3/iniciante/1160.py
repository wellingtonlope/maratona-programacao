# -*- coding: utf-8 -*-

t = int(input())

for i in range(t):
    pa, pb, g1, g2 = map(float, input().split())
    g1 = g1/100 + 1
    g2 = g2/100 + 1

    anos = 0
    while pa <= pb:
        pa = int(pa*g1)
        pb = int(pb*g2)
        anos += 1
        if anos > 100:
            break

    print('Mais de 1 seculo.') if anos > 100 else print('%i anos.' % anos)
