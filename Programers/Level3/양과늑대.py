#10/23

def dfs(status, graph, info, visited, n) :
    global answer

    if visited[status] :
        return
    
    visited[status] = True
    
    lamb,wolf = 0,0
  
    for i in range(n) :

        if status & (1 << i) :
            if info[i] == 0 :
                lamb += 1
            else:
                wolf += 1
     
    if wolf >= lamb :
        return
        
    answer = max(answer, lamb)
 
    for i in range(n) :

        if status & (1 << i) :
            for node in graph[i] :
                if not status & (1 << node) :
                    dfs(status | (1 << node), graph, info, visited, n)

answer = 0

def solution(info, edges):
    global answer
    n = len(info)
    graph = [[] for _ in range(n)]
    visited = [0] * (1 << n)
    
    for info in edges :
        graph[info[0]].append(info[1])
        

    dfs(1, graph, info, visited, n)
    return answer
