import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
    
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
        
def bfs(n):
    q = deque([n])
   
    while q:
        temp = q.popleft()
            
        for x in graph[temp]:
            if visited[x] == False:
                visited[x] = True
                q.append(x)
             
        
for i in range(1, n+1):
     if visited[i] == False:
        bfs(i)
        answer +=1
        
print(answer)