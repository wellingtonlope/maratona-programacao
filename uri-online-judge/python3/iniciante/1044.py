# -*- coding: utf-8 -*-

a, b = map(int, input().split())

print('Sao Multiplos' if a % b == 0 or b % a == 0 else 'Nao sao Multiplos')
