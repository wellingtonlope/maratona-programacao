# -*- coding: utf-8 -*-

lanches = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

codigo, quantidade = list(map(float, input().split()))

print('Total: R$ {:.2f}'.format(lanches[codigo] * quantidade))
