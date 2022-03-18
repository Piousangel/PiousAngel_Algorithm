from collections import deque
import sys
import copy

dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = 0

def bfs():
    global answer
    boardCopy = copy.deepcopy(board)
    for i in range(row):
        for j in range(col):
            if boardCopy[i][j] == 2:
                q.append([i,j])
                
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx and nx < col and 0 <= ny and ny < row:
                if boardCopy[ny][nx] == 0 :
                    boardCopy[ny][nx] = 2
                    q.append([ny,nx])
    maxVal = 0                
    for line in boardCopy:
        maxVal += line.count(0)
        
    answer = max(answer, maxVal)

def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(cnt+1)
                board[i][j] = 0

row, col = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
q = deque()
dfs(0)
print(answer)