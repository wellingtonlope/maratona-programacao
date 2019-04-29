# -*- coding: utf-8 -*-

i = 1
j = 7
while i <= 9:
    print('I=%i J=%i' % (i, j))
    if j == 5:
        i += 2
        j = 7
    else:
        j -= 1
