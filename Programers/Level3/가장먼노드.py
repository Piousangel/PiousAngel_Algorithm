from collections import deque


def chkDistance(graph, visited, start) :
  
    q = deque()
    q.append([start, 0])
    
    while q :
        
        now, cnt = q.popleft()
        
        if visited[now] == -1 :
            visited[now] = cnt
   
            for node in graph[now] :
                q.append([node, cnt+1])
    
def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
 
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    
    # print(graph)
    chkDistance(graph, visited, 1)
    
    for value in visited :
        if value == max(visited):
            answer += 1
    
    return answer