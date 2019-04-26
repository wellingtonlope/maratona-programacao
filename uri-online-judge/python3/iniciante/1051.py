# -*- coding: utf-8 -*-

salario = float(input())
imposto = 0
isento = False

if salario <= 2000:
    isento = True

if salario > 4500:
    imposto += (salario - 4500) * 0.28
    salario = 4500
if salario > 3000:
    imposto += (salario - 3000) * 0.18
    salario = 3000
if salario > 2000:
    imposto += (salario - 2000) * 0.08

print('Isento' if isento else 'R$ %.2f' % imposto)
