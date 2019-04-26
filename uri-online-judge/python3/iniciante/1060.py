# -*- coding: utf-8 -*-

positivos = 0

for i in range(6):
    positivos += 1 if float(input()) > 0 else 0

print('%i valores positivos' % positivos)
