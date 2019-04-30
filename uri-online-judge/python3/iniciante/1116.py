# -*- coding: utf-8 -*-

for i in range(int(input())):
    x, y = map(float, input().split())
    try:
        print('%.1f' % (x/y))
    except:
        print('divisao impossivel')
