import sys
sys.setrecursion(10**7)
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

graph = [ [] for _ in range(n+1)]
parent = [0] * (n+1)
visited = [False] * (n+1)

for i in range(n-1) :
    n1, n2 = map(int, input().split())

    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(node, visited, parent, graph, idx) :

    if idx == N :
        return
    
    for temp in graph[node] :

        if visited[temp] != True :
            visited[temp] = True
            parent[temp] = node 
            dfs(temp, visited, parent, graph, idx + 1)

dfs(1, visited, parent, graph, 0)

for i in range(2, len(parent)):
    print(parent)
    