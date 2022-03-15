n_list = []
box = [0]*2
visited = [0]*2
total = 0
for i in range(9):
    n_list.append(int(input()))

total = sum(n_list)

def chkIdx(box):
    for i in range(len(box)):
        print(box[i])

def dfs(n_list, box, visited, r, idx):
    if(idx == r):
        chkIdx(box)
        return
    
    for i in range(len(n_list)):
        if visited[i] == 0:
            visited[i] = 1
            box[idx] = n_list[i]
            dfs(n_list, box, visited, r, idx+1)
            visited[i] = 0

dfs(n_list,box, visited, 2, 0)