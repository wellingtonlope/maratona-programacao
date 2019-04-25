# -*- coding: utf-8 -*-

inicio, fim = map(int, input().split())

if inicio >= fim:
    horas = (fim + 24) - inicio
else:
    horas = fim - inicio

print('O JOGO DUROU %i HORA(S)' % horas)
