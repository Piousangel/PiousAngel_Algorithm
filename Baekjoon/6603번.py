def printf(box, visited):
    for i in range(len(box)):
        if visited[i] == 1:
            print(box[i], end=' ')
    print()

def dfs(n_list, box, visited, start, idx, r):
    if idx == r:
        printf(n_list,visited)
        return
    
    for i in range(start, len(n_list)):
        if visited[i] == 0:
            visited[i] = 1
            #box[idx] = n_list[i]
            dfs(n_list, box, visited, i+1, idx+1, r)
            visited[i] = 0
          

while True:
    n_list = list(map(int, input().split()))
    if len(n_list) == 1:
        break
        
    c = n_list[0]
    del n_list[0]
    visited = [0] * c
    box = [0] * c
    dfs(n_list, box, visited, 0,0,6)
    print()
