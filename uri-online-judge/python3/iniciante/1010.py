# -*- coding: utf-8 -*

pecas = []
pecas.append(list(input().split()))
pecas.append(list(input().split()))

total = 0
for peca in pecas:
    total += int(peca[1]) * float(peca[2])

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
