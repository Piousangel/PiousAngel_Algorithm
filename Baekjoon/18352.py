import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, m, k, x = map(int, input().split()) #도시 수, 도로 개수, 거리 정보, 출발도시

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

answer = []
def bfs(graph, distance, start_point) :

    q = deque()
    q.append([start_point, 0])
    visited[start_point] = True
    while q :

        now, idx = q.popleft()

        if idx == distance :
            answer.append(now)

        for i in graph[now] :
            if visited[i] != True :
                visited[i] = True
                q.append([i, idx+1])


bfs(graph, k, x)

if len(answer) == 0 :
    print("-1")
else:
    answer.sort()
    for i in answer :
        print(i)

