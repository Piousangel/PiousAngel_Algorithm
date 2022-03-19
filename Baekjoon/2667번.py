from collections import deque
n = int(input())

board = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

h_list = []

def bfs(board, visited, i, j):
    cnt = 1
    q = deque()
    q.append([i,j])
    visited[i][j] = True
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0 <=ny<n and board[ny][nx] == '1':
                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append([ny,nx])
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if visited[i][j] == False and board[i][j] == '1':
            h_list.append(bfs(board, visited, i, j))
                
print(len(h_list))
h_list.sort()
for i in h_list:
    print(i)