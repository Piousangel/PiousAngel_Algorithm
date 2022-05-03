def findmaxLamb(graph, visited, info, idx, life, lambCnt) :
    global answer
    print("idx", idx)
    print("life", life)
    print("lambCnt", lambCnt)

    answer = max(answer, lambCnt)
    
    for node in graph[idx] :
        if visited[node] != True and life + info[node] > 0:
            if info[node] == 1:
                life += 1   #양과 늑대수의 합을 구하려고
                lambCnt += 1
            else:
                life -= 1
               
            if life > 0 :
                visited[node] = True
                findmaxLamb(graph, visited, info, node, life, lambCnt)
                visited[node] = False
    
    return answer

answer = 0

def solution(info, edges):
    global answer
    n = len(info)
    graph = [[] for i in range(n)]
    newInfo = []
    for i in info :
        if i == 0:
            newInfo.append(1)
        else:
            newInfo.append(-1)
    visited = [False] * n
    
    for edge in edges :
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        
    visited[0] = True
    answer = findmaxLamb(graph, visited, newInfo, 0, 1, 1)
    
    return answer