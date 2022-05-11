import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, m = map(int, input().split())  #n 행, m 열

board = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[-1]*m for _ in range(n)]
for i in range(n) :
    board.append(list(input().rstrip()))

def bfs(board, visited) :

    q = deque()
    q.append([0,0])
    visited[0][0] = 1

    while q :

        y, x = q.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n :
                if visited[ny][nx] == -1 and board[ny][nx] == '1' :
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny,nx])

bfs(board, visited)
print(visited[-1][-1])