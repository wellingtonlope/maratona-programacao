# -*- coding: utf-8 -*-

total = 0
inter = 0
gremio = 0

while True:
    golInter, golGremio = map(int, input().split())
    inter += 1 if golInter > golGremio else 0
    gremio += 1 if golInter < golGremio else 0
    total += 1

    grenal = int(input('Novo grenal (1-sim 2-nao)\n'))
    if grenal == 2:
        break

print(str(total) + ' grenais')
print('Inter:' + str(inter))
print('Gremio:' + str(gremio))
print('Empates:' + str(total - (inter + gremio)))

if inter > gremio:
    print('Inter venceu mais')
elif inter < gremio:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
