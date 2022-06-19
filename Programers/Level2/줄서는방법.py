# 시간 초과

def chk(arr) :
    global answer
    for a in arr :
        answer.append(a)

def dfs(temp, arr, visited, idx, n, k) :
    global chkcnt

    if idx == n :
        chkcnt += 1
        if chkcnt == k :
            chk(arr)
            return

    for i in range(len(arr)) :
        if visited[i] == False :
            visited[i] = True
            arr[idx] = temp[i]
            dfs(temp, arr, visited, idx+1, n, k)
            visited[i] = False

chkcnt = 0
answer = []
def solution(n, k):
    global answer

    temp = []
    arr = [0] * n
    
    visited = [False] * (n+1)
    for i in range(1, n+1) :
        temp.append(i)
        
    dfs(temp, arr, visited, 0, n, k)
    
    return answer