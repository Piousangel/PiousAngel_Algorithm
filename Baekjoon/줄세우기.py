import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
answer_list = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    visited[b] +=1

 
def top_sort(graph, visited) :

    q = deque()

    for i in range(1, len(visited)):
        if visited[i] == 0 :
            answer_list.append(i)
            q.append(i)

    while q :

        now_idx = q.popleft()

        for k in range(len(graph[now_idx])) :  # 어차피 한바퀴만 돔
            # print(graph[now_idx][k])
            visited[graph[now_idx][k]] -= 1

            if visited[graph[now_idx][k]] == 0 :
                answer_list.append(graph[now_idx][k])
                q.append(graph[now_idx][k])


top_sort(graph, visited)

for i in answer_list :
    print(i, end=" ")