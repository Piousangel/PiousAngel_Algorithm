n,r = map(int, input().split())

arr = list(range(1,n+1))
box = [0] * r
visited = [0 for _ in range(n)]

def showBox(arr):
    for x in arr:
        print(x, end=' ')
    print()
            
def dfs(arr, box, visited, n, r, idx):
    if(r == 0):
        showBox(box)
        return
    
    for i in range(len(arr)):
        if visited[i] == 0:
            box[idx] = arr[i]
            dfs(arr, box, visited, n, r-1, idx+1)
            
dfs(arr, box, visited, n, r, 0)