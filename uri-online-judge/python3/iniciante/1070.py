# -*- coding: utf-8 -*-

x = int(input())

[print(i) for i in range(x if x % 2 == 1 else x + 1, x + 12, 2)]
