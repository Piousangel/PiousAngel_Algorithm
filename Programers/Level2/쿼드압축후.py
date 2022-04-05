answer = [0, 0]

def isBlock(arr, aLen, row, col):
    for i in range(row, row+aLen):
        for j in range(col, col+aLen):
            if arr[i][j] != arr[row][col]:
                return False
    answer[arr[row][col]] += 1
    return True

def dfs(arr, aLen, row, col):
    
    if aLen == 1 :
        # if arr[row][col] == 0 :
        #     answer[0] += 1
        # if arr[row][col] == 1:
        #     answer[1] += 1
        answer[arr[row][col]] += 1
        return
    
    if isBlock(arr, aLen, row, col):
        return
            
    dfs(arr, aLen//2, row, col)
    dfs(arr, aLen//2, row, col + aLen//2)
    dfs(arr, aLen//2, row + aLen//2, col)
    dfs(arr, aLen//2, row + aLen//2, col + aLen//2)

def solution(arr):
    arr_len = len(arr)
    dfs(arr, arr_len, 0, 0)
    return answer