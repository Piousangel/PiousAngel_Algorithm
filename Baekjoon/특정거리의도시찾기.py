import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, M, K, X = map(int, input().split()) # k 거리, x 출발 도시 정보

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, visited, K, X, answer_list) :

    q = deque()
    q.append([X,0])
    visited[X] = True

    while q :

        now, cnt = q.popleft()

        if cnt == K :
            answer_list.append(now)

        for i in graph[now] :
            if visited[i] == False :
                visited[i] = True
                q.append([i,cnt+1])
    

answer_list= []
bfs(graph, visited, K, X, answer_list)

if len(answer_list) == 0 :
    print("-1")
else:
    answer_list.sort()
    for i in answer_list :
        print(i)
