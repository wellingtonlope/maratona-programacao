# -*- coding: utf-8 -*-

horaInicio, minutoInicio, horaFim, minutoFim = map(int, input().split())
hora, minuto = [0, 0]

if horaInicio >= horaFim:
    hora = (24 + horaFim) - horaInicio
else:
    hora = horaFim - horaInicio

if minutoInicio > minutoFim:
    minuto = (60 + minutoFim) - minutoInicio
    hora -= 1
else:
    minuto = minutoFim - minutoInicio
    if minuto != 0 and horaInicio == horaFim:
        hora = 0

print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' % (hora, minuto))
