# -*- coding: utf-8 -*

valor = int(input())

print(valor)
print('{} nota(s) de R$ 100,00'.format(int(valor/100)))
valor %= 100
print('{} nota(s) de R$ 50,00'.format(int(valor/50)))
valor %= 50
print('{} nota(s) de R$ 20,00'.format(int(valor/20)))
valor %= 20
print('{} nota(s) de R$ 10,00'.format(int(valor/10)))
valor %= 10
print('{} nota(s) de R$ 5,00'.format(int(valor/5)))
valor %= 5
print('{} nota(s) de R$ 2,00'.format(int(valor/2)))
valor %= 2
print('{} nota(s) de R$ 1,00'.format(int(valor)))