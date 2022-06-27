import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

r, c = map(int, input().split())

dy = [-1, 0, 1]

board = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

def dfs(y, x) :
    if x == c - 1 : #오른쪽 끝까지 잘 도착했을 경우
        return True

    for k in range(3):
        ny = y + dy[k]

        if 0 <= ny < r and board[ny][x+1] == '.' and not visited[ny][x+1]:
            visited[ny][x+1] = True
            temp = dfs(ny, x+1)
            if temp :
                return True
                
    return False

answer = 0

for i in range(r) :
    if board[i][0] == '.':
        if dfs(i, 0) :
            answer += 1

print(answer)
