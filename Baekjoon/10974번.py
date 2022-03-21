n = int(input())

arr = [i for i in range(1,n+1)]
box = [0] * n
visited = [False] * n

def printf(box):
    for x in box:
        print(x, end=" ")
    print()

def dfs(arr, box, visited,idx, n):
    if idx == n:
        printf(box)
        return
        
    for i in range(0, len(arr)):
        if visited[i] == False:
            visited[i] = True
            box[idx] = arr[i]
            dfs(arr, box, visited, idx+1, n)
            visited[i] = False

dfs(arr, box, visited, 0, n)