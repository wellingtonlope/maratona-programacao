# -*- coding: utf-8 -*-

n = int(input())
carlos = int(input())
venceu = True

for i in range(n - 1):
    if int(input()) > carlos:
        venceu = False

print('S' if venceu else 'N')
