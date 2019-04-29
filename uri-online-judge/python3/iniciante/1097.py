# -*- coding: utf-8 -*-

i = 1
j = 7
aux = 5
while i <= 9:
    print('I=%i J=%i' % (i, j))
    if j == aux:
        i += 2
        aux += 2
        j += 4
    else:
        j -= 1
