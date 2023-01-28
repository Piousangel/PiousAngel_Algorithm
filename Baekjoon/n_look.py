
def dfs(row, n, board, visited, k) :
    if row == k :
        answer += 1
        return
    else:
        for i in range(n):
            if visited[i] != 1 :
                board[row][i] = 1
                visited[col] = 1
                dfs(row + 1, n, board, visited, k)
                board[row][i] = 0
                visited[col] = 0

answer = 0
solution(n, k) :
    global answer
    board = [[0 for _ in range(n)] for _ in range(n)]
    visited = [0] * n

    dfs(0, n, board, visited, k)

    return answer
