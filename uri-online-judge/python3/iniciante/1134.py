# -*- coding: utf-8 -*-

alcool = 0
gasolina = 0
diesel = 0

while True:
    alternativa = int(input())
    alcool += 1 if alternativa == 1 else 0
    gasolina += 1 if alternativa == 2 else 0
    diesel += 1 if alternativa == 3 else 0

    if alternativa == 4:
        break

print('MUITO OBRIGADO')
print('Alcool:', alcool)
print('Gasolina:', gasolina)
print('Diesel:', diesel)
