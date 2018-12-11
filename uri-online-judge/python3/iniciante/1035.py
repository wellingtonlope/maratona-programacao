# -*- coding: utf-8 -*-

a, b, c, d = list(map(int, input().split()))

if (b > c and d > a and c + d > a + b and c > 0 and d > 0):
  print('Valores aceitos')
else:
  print('Valores nao aceitos')
