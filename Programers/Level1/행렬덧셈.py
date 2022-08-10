def solution(arr1, arr2):
    
    row = len(arr1)
    col = len(arr1[0])
    
    answer = [ [0] * col for _ in range(row) ]
        
    # print(answer)
    
    for i in range(row) :
        for j in range(col) :
            # print(arr1[i][j] + arr2[i][j])
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer