import copy

answer = -1
def solution(k, dungeons):
    
    let visited =  Array(dungeons.length).fill(-1)
    
    dfs(dungeons, visited, k, 0)
    return answer
    
#[:] list.deepcopy
def dfs(dungeons, visited, k, cnt):
    # visited2 = copy.deepcopy(visited)
    # dungeons2 = copy.deepcopy(dungeons)
    for i in range(len(dungeons)):
        if visited[i] != 0 and k >= dungeons[i][0]:
            visited[i] = 0
            dfs(dungeons, visited, k-dungeons[i][1], cnt +1)
            visited[i] = -1
            
    global answer
    answer = max(answer, cnt)
    
# answer = -1

# def solution(k, dungeons):
    
#     global answer
#     visited = [-1 for _ in range(len(dungeons))]
    
#     dfs(dungeons, visited, k, 0)
#     return answer
    
# #[:] list.deepcopy
# def dfs(dungeons, visited, k, cnt):
#     visited2 = copy.deepcopy(visited)
#     dungeons2 = copy.deepcopy(dungeons)
#     for i in range(len(dungeons)):
#         if visited2[i] != 0 and k >= dungeons2[i][0]:
#             visited2[i] = 0
#             dfs(dungeons2, visited2, k-dungeons2[i][1], cnt +1)
#             visited2[i] = -1
            
#     global answer
#     answer = max(answer, cnt)


