import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    visited[b] += 1


def top_sort(graph, visited, answer_list) :

    q = deque()
    for i in range(1, n+1) :
        if visited[i] == 0 :
            answer_list.append(i)
            q.append(i)

    while q :
  
        now = q.popleft()

        for node in graph[now] :
            visited[node] -= 1

            if visited[node] == 0 :
                answer_list.append(node)
                q.append(node)




answer_list = []
top_sort(graph, visited, answer_list)
    
for i in answer_list :
    print(i, end=" ")
