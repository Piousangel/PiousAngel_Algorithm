import sys
n, total = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
visited = [False] * n
cnt = 0
    
def chkT(n_list, visited):
    global cnt
    sumN = 0
    for i in range(len(n_list)):
        if visited[i] == True:
            sumN += n_list[i]
            if sumN == total:
                cnt += 1
    
def dfs(n_list, visited, start, idx, r):
    if idx == r:
        chkT(n_list, visited)
        return
            
    for i in range(start, len(n_list)):
        if visited[i] == False:
            visited[i] = True
            dfs(n_list, visited, i+1, idx+1, r)
            visited[i] = False
            
for i in range(1, n+1):
    dfs(n_list, visited, 0, 0, i)
        
print(cnt)