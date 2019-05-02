# -*- coding: utf-8 -*-

n = []
[n.append(int(input())) for i in range(20)]

n.reverse()

[print('N[%i] = %i' % (i, n[i])) for i in range(20)]
