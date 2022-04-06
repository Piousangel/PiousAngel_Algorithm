def chkSosu(arr):
    global answer
    sosu_list = [False] * 10000000
    sosu_list[0] = True
    sosu_list[1] = True
    temp = ''
    for i in range(len(arr)):
        temp += arr[i]
    temp_int = int(temp)
    
   
    for i in range(2, 10001):
        for j in range(i+i, 10000000, i):
            sosu_list[j] = True
    
    if sosu_list[temp_int-1] == False:
        answer +=1
    
    return

def dfs(n_list, box, visited, idx, lenOfNum):
    
    if idx == lenOfNum:
        chkSosu(box)
        return
        
    for i in range(0, len(n_list)):
        if visited[i] != True:
            visited[i] = True
            box[idx] = n_list[i]
            dfs(n_list, box, visited, idx+1, lenOfNum)
            visited[i] = False

answer = 0
def solution(numbers):
    global answer
    
    n_list = []
    
    for i in numbers:
        n_list.append(i)
    
    visited = [False] * len(n_list)
    
    for i in range(1, len(n_list)+1):
        box = [0] * i
        dfs(n_list, box, visited, 0 , i)
        
    return answer