# -*- coding: utf-8 -*-

x = int(input())

[print(i) for i in range(1, x if x % 2 == 0 else x + 1, 2)]
