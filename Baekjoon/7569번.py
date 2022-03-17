from collections import deque
import sys

col, row, h = map(int, input().split())
dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]
answer = 0
#board = [list(map(int, input().split())) for _ in range(row)]
board = []
q = deque([])

def bfs(board):
    global col,row,h
    
    while q:
        x, y, z = q.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx and nx < h and 0 <= ny and ny < row and 0 <= nz and nz < col :
                if board[nx][ny][nz] == 0:
                    board[nx][ny][nz] = board[x][y][z] +1
                    q.append([nx,ny,nz])

for i in range(h):  
    temp = []
    for j in range(row):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(col):
            if board[j][k] == 1:
                q.append([i,j,k])
        board.append(temp)

bfs(board)

for i in board:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))

print(answer-1)