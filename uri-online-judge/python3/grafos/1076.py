# -*- coding: utf-8 -*-


def dfs(graph, node, visited):
    global count
    if node not in visited:
        visited.append(node)
        for no in graph[node]:
            count += 1
            dfs(graph, no, visited)
    return visited


for i in range(int(input())):
    count = 0
    n = int(input())
    v, a = map(int, input().split())

    graph1 = []
    for j in range(v):
        graph1.append([])

    for j in range(a):
        v1, v2 = map(int, input().split())
        if v1 not in graph1[v2]:
            graph1[v1].append(v2)
            graph1[v2].append(v1)

    dfs(graph1, n, [])
    print(count)
