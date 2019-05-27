# -*- coding: utf-8 -*-


def jogo(sheldon, raj):
    if sheldon == raj:
        return 'De novo!'
    if sheldon == 'tesoura' and raj == 'papel' \
        or sheldon == 'papel' and raj == 'pedra' \
        or sheldon == 'pedra' and raj == 'lagarto' \
        or sheldon == 'lagarto' and raj == 'Spock' \
        or sheldon == 'Spock' and raj == 'tesoura' \
        or sheldon == 'tesoura' and raj == 'lagarto' \
        or sheldon == 'lagarto' and raj == 'papel' \
        or sheldon == 'papel' and raj == 'Spock' \
        or sheldon == 'Spock' and raj == 'pedra' \
        or sheldon == 'pedra' and raj == 'tesoura':
        return 'Bazinga!'
    else:
        return 'Raj trapaceou!'


for t in range(int(input())):
    sheldon, raj = input().split()
    print('Caso #%i: %s' % (t + 1, jogo(sheldon, raj)))
