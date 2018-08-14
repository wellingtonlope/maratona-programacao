# -*- coding: utf-8 -*

tempo = int(input())
velocidade = int(input())

consumo = (tempo * velocidade) / 12

print('{:.3f}'.format(consumo))