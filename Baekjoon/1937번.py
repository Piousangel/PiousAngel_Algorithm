import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('sample.txt')
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

# print(board)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

arr = [[-1] * n for _ in range(n)]

def dfs(y, x) :
    # global board, arr

    if arr[y][x] == -1:
        arr[y][x] = 0

        for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx <= n-1 and 0 <= ny <= n-1 :
                    if board[ny][nx] > board[y][x] :
                        arr[y][x] = max(arr[y][x], dfs(ny,nx))
    return arr[y][x]+1

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i,j))

print(answer)
