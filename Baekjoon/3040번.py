n_list = []

for i in range(9):
    n_list.append(int(input()))
    
box = [0]*7
visited = [0] * 9

def bfs(n_list, box, visited, start, idx, r):
    if idx == r:
        sumN = sum(box)
        if sumN == 100:
            for x in box:
                print(x)
        return 
    
    for i in range(start, len(n_list)):
        if visited[i] == 0:
            visited[i] = 1
            box[idx] = n_list[i]
            bfs(n_list, box, visited, i+1, idx+1, r)
            visited[i] = 0

bfs(n_list, box, visited, 0,0,7)