n = int(input())
answer = 0

def isPossible(col, row):
    for i in range(row):
        if col[i] == col[row]:
            return False
        if abs(i-row) == abs(col[i]-col[row]):
            return False
    return True

def dfs(col, row):
    global answer
    if row == len(col)-1:
        answer += 1
    else:
        for i in range(len(col)):
            col[row+1] = i
            if(isPossible(col, row+1)):
                dfs(col, row+1)

for i in range(n):
    col = [0]*n
    col[0] = i
    dfs(col, 0)
    print(answer)