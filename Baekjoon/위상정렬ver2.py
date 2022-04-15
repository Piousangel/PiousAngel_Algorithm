from collections import deque

n, v = map(int, input().split()) #노드, 간선


graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(v):
    a, b = map(int, input().split())

    graph[a].append(b)
    indegree[b] += 1


def topology_sort():

    arr = []
    q = deque()

    for i in range(1, len(indegree)):
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        arr.append(now)

        for i in range(len(graph[now])):
            indegree[graph[now][i]] -= 1
        
            if indegree[graph[now][i]] == 0:
                q.append(graph[now][i])

    for i in arr :
        print(i, end= ' ')

topology_sort()