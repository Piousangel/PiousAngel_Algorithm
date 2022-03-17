import copy
import sys

row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

max_value = 0

def chk_virus(r,c, board):
    if board[r][c] == 2:
        
        for i in range(4):
            
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr and nr < row and 0 <= nc and nc < col:
                if board[nr][nc] == 0:
                    board[nr][nc] = 2
                    chk_virus(nr, nc, board)

def dfs(start, cnt):
    global max_value
    if cnt == 3:
        copy_board = copy.deepcopy(board)
        for r in range(row):
            for c in range(col):
                chk_virus(r,c, copy_board)
        safe_cnts = sum(i.count(0) for i in copy_board)
        max_value = max(max_value, safe_cnts)
        return True
    else:
        for i in range(start, row*col):
            r = i//col
            c = i % col
            if board[r][c] == 0:
                board[r][c] = 1
                dfs(i, cnt+1)
                board[r][c] = 0
                
dfs(0,0)
print(max_value)