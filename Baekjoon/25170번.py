import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

row, col, time = map(int, input().split()) # 격자 크기와 남은 시간

can_board = []
time_board = []
visited = [[False] * col for _ in range(row)]

for i in range(row) :
    can_board.append(list(map(int, input().split())))
for i in range(row) :
    time_board.append(list(map(int, input().split())))

# print(can_board)
# print(time_board)
# print(visited)

def bfs(can_board, time_board, visited, time) :
    global answer
    q = deque()
    q.append([0, 0, time, 0])
    visited[0][0] = True

    while q :

        y, x, now_time, total = q.popleft()
        
        if x == len(can_board[0]) - 1 and y == len(can_board) :
            answer = max(answer, total)
            return 

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(can_board[0]) and 0 <= ny < len(can_board) and now_time - time_board[ny][nx] >= 0 :
                if visited[ny][nx] != True :
                    visited[ny][nx] = True
                    q.append([ny, nx, now_time - time_board[ny][nx], total + can_board[ny][nx]])

    answer = max(answer, total)

answer = 0
bfs(can_board, time_board, visited, time)
print(answer)