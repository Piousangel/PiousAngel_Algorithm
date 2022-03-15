n,r = map(int, input().split())

arr = list(range(1,n+1))
visited = [0 for _ in range(n)]

def showBox(arr, visited, n):
    for i in range(0,n):
        if(visited[i] == 1):
            print(arr[i], end=" ")
    print()
            
def dfs(arr, visited, n, r, idx):
    if(r == 0):
        showBox(arr, visited, n)
        return
    
    for i in range(idx, n):
        visited[i] = 1
        dfs(arr, visited, n, r-1, i+1)
        visited[i] = 0
            
dfs(arr, visited, n, r, 0)
