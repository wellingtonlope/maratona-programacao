# -*- coding: utf-8 -*-


def fib(num):
    at = 0
    an = 1
    if num == 0:
        return 0
    for i in range(num):
        aux = at
        at = an + aux
        an = aux
    return at


n = []
for i in range(int(input())):
    n.append(int(input()))

for i in n:
    print('Fib(%i) = %i' % (i, fib(i)))
