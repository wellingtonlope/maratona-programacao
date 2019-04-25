# -*- coding: utf-8 -*-

estrelas = int(input())
carneiros = list(map(int, input().split()))

total_carneiros = sum(carneiros)
roubados = 0
aux = 0
estrelas_roubadas = 0

while(aux >= 0 and aux < estrelas):
    if(carneiros[aux] == 0):
        break
    if(aux > estrelas_roubadas):
        estrelas_roubadas = aux

    roubados += 1
    if(carneiros[aux] % 2 == 0):
        carneiros[aux] -= 1
        aux -= 1
    else:
        carneiros[aux] -= 1
        aux += 1

nao_roubados = total_carneiros - roubados

print('%i %i' % (estrelas_roubadas + 1, nao_roubados))
