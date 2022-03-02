import math
def solution(board):
    answer = 0
    
    arr = [[0 for c in range(len(board[0])+1)] for c in range(len(board)+1)]
    
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            arr[i+1][j+1] = board[i][j]
    
    for i in range(len(arr)) :
        for j in range(1, len(arr[0])) :
            if(arr[i][j] != 0) :
                arr[i][j] = min(min(arr[i][j-1], arr[i-1][j]), arr[i-1][j-1]) +1
                answer = max(answer, arr[i][j])
    
    return answer * answer
   