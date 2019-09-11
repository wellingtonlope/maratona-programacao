# -*- coding: utf-8 -*-
input()  # string
int(input())  # int
float(input())  # float
print('%s, %i, %.2f' % ('hello', 1, 3.14))
2 ** 3 == 8
9 ** (1 / 3)
8 ** (1 / 2)

# lista
len([3, 2, 1])  # 3
[1] * 2  # [1,1]
1 in [1, 2, 3]  # True
min([1, 2, 3])  # 1
max([1, 2, 3])  # 3
sum([1, 2, 3])  # 6
vetor = []
vetor.insert(0, 2)  # insere 2 an posição 0
vetor.append(4)  # adiciona 4 ao final do vetor
vetor.index(3)  # pesquisa pelo conteudo e retorna o index
vetor.pop()  # retorna o ultimo valor e exclui o mesmo
vetor.pop(0)  # retorna o valor do index escolhido e apaga o mesmo
vetor.remove('Wellington')  # exclui o item especificado
vetor.reverse()  # ordem decrescente
vetor.sort()  # ordem crescente
vetor.count('valor')  # informa a quantidade de vezes que o item aparece no vetor
valores = list(map(float, input().split()))
a, b, c = map(float, input().split())
itens = [1, 2, 3]
for item in itens:
    print('item: %s' % item)
for index in range(1, 3):  # 1 ao 2
    [print(valor) for valor in valores]
sorted([1, 2, 3], reverse=True)  # reverse por padrão é False
str(3.14)  # string
print('True' if True else 'False')
[print(numero) for numero in range(2, 101, 2)]  # inicio, fim, passo
' 3.14 '.strip()  # '3.14'
', '.join(map(str, [1, 2, 3])) # 1, 2, 3
'1,2,3'.index('2') # buscar valor na string
'AbA'.swapcase() # aBa
'arroz feijao'.title() # Arroz Feijao

# leia até EOF
while True:
    try:
        input()
    except EOFError:
        break

# grafos
# busca em profundidade
def dfs(graph, node, visited):
    global count
    if node not in visited:
        visited.append(node)
        for no in graph[node]:
            count += 1
            dfs(graph, no, visited)
    return visited
