from collections import deque
col, row = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(row)]
q = deque([])
dx = [0,0,1,-1]
dy = [1,-1,0,0]

answer = 0

def bfs(board):
   
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx and nx < len(board[0]) and 0 <= ny and ny < len(board):
                if board[ny][nx] == 0:
                    board[ny][nx] = board[y][x] +1
                    q.append([ny,nx])
    
for i in range(row):
    for j in range(col):
        if board[i][j] == 1:
            #bfs(board, i, j)
            q.append([i,j])
                
bfs(board)
 
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))
    
print(answer-1) 