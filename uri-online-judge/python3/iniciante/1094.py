# -*- coding: utf-8 -*-

coelhos = 0
ratos = 0
sapos = 0

for i in range(int(input())):
    quantidade, tipo = input().split()
    coelhos += int(quantidade) if tipo == 'C' else 0
    ratos += int(quantidade) if tipo == 'R' else 0
    sapos += int(quantidade) if tipo == 'S' else 0

total = coelhos + ratos + sapos
print('Total: %i cobaias' % total)
print('Total de coelhos: %i' % coelhos)
print('Total de ratos: %i' % ratos)
print('Total de sapos: %i' % sapos)
print('Percentual de coelhos: %.2f %%' % ((coelhos * 100) / total))
print('Percentual de ratos: %.2f %%' % ((ratos * 100) / total))
print('Percentual de sapos: %.2f %%' % ((sapos * 100) / total))
