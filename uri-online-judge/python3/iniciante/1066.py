# -*- coding: utf-8 -*-

pares = 0
positivos = 0
negativos = 0

for i in range(5):
    entrada = int(input())
    pares += 1 if entrada % 2 == 0 else 0
    positivos += 1 if entrada > 0 else 0
    negativos += 1 if entrada < 0 else 0

print('%i valor(es) par(es)' % pares)
print('%i valor(es) impar(es)' % (5 - pares))
print('%i valor(es) positivo(s)' % positivos)
print('%i valor(es) negativo(s)' % negativos)
