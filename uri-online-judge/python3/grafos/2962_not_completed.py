# -*- coding: utf-8 -*-

impedimento = False


def sensor(salao, x, y, s):
    xInicio = 0 if x - s else x - s
    xFim = len(salao) - 1 if len(salao) <= x + s - 1 else x + s - 1
    yInicio = 0 if y - s else y - s
    yFim = len(salao[0]) - 1 if len(salao[0]) <= y + s - 1 else y + s - 1
    for i in range(xInicio, xFim):
        for j in range(yInicio, yFim):
            salao[i][j] = 0
    mostrar(salao)
    imp(salao, x, y, s)


def imp(salao, x, y, s):
    global impedimento
    xInicio = 0 if x - s else x - s
    xFim = len(salao) - 1 if len(salao) <= x + s - 1 else x + s - 1
    yInicio = 0 if y - s else y - s
    yFim = len(salao[0]) - 1 if len(salao[0]) <= y + s - 1 else y + s - 1

    for i in range(xInicio, xFim):
        for j in range(n):
            if salao[i][j] != 0:
                break
            if j == n - 1:
                impedimento = True
        if impedimento:
            break

    if not impedimento:
        for j in range(yInicio, yFim):
            for i in range(m):
                if salao[i][j] != 0:
                    break
                if i == m - 1:
                    impedimento = True
            if impedimento:
                break


def mostrar(salao):
    for i in salao:
        print(i)
    print()


m, n, k = map(int, input().split())

salao = [[1 for col in range(n)] for row in range(m)]

for i in range(k):
    x, y, s = map(int, input().split())
    sensor(salao, x, y, s)

mostrar(salao)
print('N' if impedimento else 'S')
