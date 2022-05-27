import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())

visited = [[-1] * n for _ in range(n)]

board = []
for i in range(n) :
    board.append(list(input().rstrip()))

# print(board)

def bfs(board, visited, n) :

    q = deque()

    q.append([0,0])
    visited[0][0] = 0

    while q :

        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if visited[ny][nx] == -1 and board[ny][nx] == '0' : #검은방
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
                elif visited[ny][nx] == -1 and board[ny][nx] == '1' : #흰방
                    visited[ny][nx] = visited[y][x]
                    q.appendleft([ny, nx])
                

bfs(board, visited, n)
print(visited[-1][-1])

