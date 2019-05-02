# -*- coding: utf-8 -*-

for n in range(int(input())):
    x = int(input())
    primo = True
    for i in range(2, x):
        if x % i == 0:
            primo = False
            break
    print('%i eh primo' % x) if primo else print('%i nao eh primo' % x)
