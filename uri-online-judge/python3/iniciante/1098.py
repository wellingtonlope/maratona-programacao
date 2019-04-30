# -*- coding: utf-8 -*-

i = 0
j = 1
aux = 3
while i <= 2:
    print('I=%.0f J=%.0f' % (i, j)) if int(round(i, 1)) == round(i, 1) else print('I=%.1f J=%.1f' % (i, j))
    if j == aux:
        i += 0.2
        aux += 0.2
        j -= 1.8
    else:
        j += 1
