# -*- coding: utf-8 -*-

diaInicio = int(input().split()[1].strip())
horaInicio, minutoInicio, segundoInicio = map(int, input().replace(' ', '').split(':'))

diaFim = int(input().split()[1].strip())
horaFim, minutoFim, segundoFim = map(int, input().replace(' ', '').split(':'))

dia = diaFim - diaInicio
hora = horaFim - horaInicio
minuto = minutoFim - minutoInicio
segundo = segundoFim - segundoInicio

if segundo < 0:
    segundo += 60
    minuto -= 1

if minuto < 0:
    minuto += 60
    hora -= 1

if hora < 0:
    hora += 24
    dia -= 1

print('%i dia(s)' % dia)
print('%i hora(s)' % hora)
print('%i minuto(s)' % minuto)
print('%i segundo(s)' % segundo)
