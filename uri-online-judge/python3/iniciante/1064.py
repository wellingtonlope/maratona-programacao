# -*- coding: utf-8 -*-

total = 0
positivos = 0

for i in range(6):
    entrada = float(input())
    if entrada > 0:
        total += entrada
        positivos += 1

print('%i valores positivos' % positivos)
print('%.1f' % (total/positivos))
