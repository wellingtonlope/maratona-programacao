# -*- coding: utf-8 -*-

salario = float(input())
novoSalario = 0
reajuste = 0
percentual = 0

if salario <= 400:
    percentual = 15
    reajuste = salario * (percentual/100)
    novoSalario = reajuste + salario
elif salario <= 800:
    percentual = 12
    reajuste = salario * (percentual/100)
    novoSalario = reajuste + salario
elif salario <= 1200:
    percentual = 10
    reajuste = salario * (percentual/100)
    novoSalario = reajuste + salario
elif salario <= 2000:
    percentual = 7
    reajuste = salario * (percentual/100)
    novoSalario = reajuste + salario
else:
    percentual = 4
    reajuste = salario * (percentual/100)
    novoSalario = reajuste + salario

print('Novo salario: %.2f' % novoSalario)
print('Reajuste ganho: %.2f' % reajuste)
print('Em percentual: ' + str(percentual) + ' %')
