# -*- coding: utf-8 -*-


def fat(num):
    if num == 1:
        return 1
    return fat(num-1) * num


n = int(input())

print(fat(n))
