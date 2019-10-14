# -*- coding: utf-8 -*-


def sensor(salao, x, y, s):
    for i in range(x - s, x + s - 1):
        for j in range(y - s, y + s - 1):
            if 0 <= i < len(salao) and 0 <= j < len(salao[0]):
                salao[i][j] = -1


def mostrar(salao):
    for i in salao:
        print(i)
    print()


def vertice(vertices, item, salao, x, y):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < len(salao) and 0 <= j < len(salao[0]) and salao[i][j] != -1 and not (i == x and j == y):
                vertices[item].append(salao[i][j])


def dfs(graph, node, end, visited):
    if node not in visited:
        visited.append(node)
        if node == end:
            return visited
        for no in graph[node]:
            dfs(graph, no, end, visited)
    return visited


m, n, k = map(int, input().split())

salao = []
count = 0
for row in range(m):
    salao.append([])
    for col in range(n):
        salao[row].append(count)
        count += 1

for i in range(k):
    x, y, s = map(int, input().split())
    sensor(salao, x, y, s)

grafo = [[] for total in range(m * n)]
mostrar(salao)
for i in range(m):
    for j in range(n):
        if salao[i][j] != -1:
            vertice(grafo, salao[i][j], salao, i, j)
            
visited = []
dfs(grafo, 0, len(grafo) - 1, visited)

print('S' if len(grafo) - 1 in visited else 'N')
