from collections import deque

def bfs(board):
    q = deque()
    global cnt
    q.append([0,0])
    
    while q:
        y, x = q.popleft()
        
        if y == row -1 and x == col-1:
            print(cnt)
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx and nx<col and 0<=ny and ny<row:
                if board[ny][nx] == '1' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny,nx])
                    cnt += 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]
row, col = map(int, input().split())
board = [ list(input()) for _ in range(row)]
visited = [[0 for _ in range(col)] for _ in range(row)]

cnt = 0
bfs(board)