import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())

board = []

for i in range(n) :
    board.append(list(map(int, input().rstrip())))

row = len(board)
col = len(board[0])

visited = [ [-1 for i in range(col)] for _ in range(row)]

def bfs(board, visited, n) :
    
    q = deque()

    q.append([0,0])
    visited[0][0] = 0

    while q :
        y, x = q.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if visited[ny][nx] == -1 and board[ny][nx] == 0 :
                    visited[ny][nx] = visited[y][x]+ 1
                    q.append([ny,nx])
                elif visited[ny][nx] == -1 and board[ny][nx] == 1 :
                    visited[ny][nx] = visited[y][x]
                    q.appendleft([ny,nx])

bfs(board, visited, n)

print(visited[-1][-1])

# print(visited)
# print(board)

# 0은 검은방, 1이 흰색 방
# 흰방으로 바꿔야할 최소 방수는?


