import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().split())
board = [list(input().rstrip()) for _ in range(row)]
visited = [ [False]*col for _ in range(row)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(s_y, s_x, board) :      #물이 움직이는 시간을 좌표마다 기록해서 나중에 고슴도치가 움
    
    q = deque()

    q.append([s_y, s_x, 0])

    while q:

        y, x, time = q.popleft()
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < col and 0 <= ny < row :
                if board[ny][nx] != 'D' and board[ny][nx] != 'S' and board[ny][nx] != 'X' and board[ny][nx] != '*':    #D, S, X, * 가 아닌 모든 점을 돌면서
                    if board[ny][nx] == '.':            #점일 때
                        board[ny][nx] = time +1   
                        q.append([ny, nx, time + 1])
                    else:                                   # or 숫자일 때 (점일때는 시간으로 초기화, 숫자면 작은 숫자로 업데이트)
                        if board[ny][nx] > time + 1 :       # 물이 퍼진시간보다 작아야 고슴도치가 갈수있죠!
                            board[ny][nx] = time +1
                            q.append([ny, nx, time + 1])
        
        board[y][x] = time


def bfs2(s_y, s_x, board, visited) :      #물이 움직이는 시간을 좌표마다 기록해서 나중에 고슴도치가 움
    global answer
    q = deque()

    q.append([s_y, s_x, 0])
    visited[s_y][s_x] = True

    while q:

        y, x, time = q.popleft()

        if board[y][x] == 'D' :
            answer = time
            return

   
            
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < col and 0 <= ny < row :
                # print(ny, nx, time)
                if visited[ny][nx] == False and board[ny][nx] != 'X' :    # 방문하지 않았고, X 가 아닌 모든 점을 돌면서
                    if board[ny][nx] == '.':
                        visited[ny][nx] = True
                        q.append([ny, nx, time+1])

                    elif board[ny][nx] == 'D' :   #만약 도착지면? 
                        q.append([ny, nx, time+1])

                    elif board[ny][nx] > time + 1 :
                        visited[ny][nx] = True
                        q.append([ny, nx, time+1])
        
   
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == '*':
            bfs(i, j, board)    #물 구하기
        
# print(board)
# print(visited)
answer = 0

for i in range(len(board)):
    for j in range(len(board[0])):
        visited = [ [False] * col for _ in range(row)]
        if board[i][j] == 'S':
            bfs2(i, j, board, visited)

if answer != 0 :
    print(answer)
else:
    print("KAKTUS")