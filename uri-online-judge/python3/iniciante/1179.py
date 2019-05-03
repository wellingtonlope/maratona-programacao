# -*- coding: utf-8 -*-


def imprimir(vetor):
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            print('par[%i] = %i' % (i, vetor[i]))
        else:
            print('impar[%i] = %i' % (i, vetor[i]))


impar = []
par = []
for i in range(15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

    if len(par) == 5:
        imprimir(par)
        par = []
    if len(impar) == 5:
        imprimir(impar)
        impar = []

    if i == 14:
        imprimir(impar)
        imprimir(par)
