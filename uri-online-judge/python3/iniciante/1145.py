# -*- coding: utf-8 -*-

x, y = map(int, input().split())

[print(i, end=' ') if i % x != 0 else print(i) for i in range(1, y + 1)]
