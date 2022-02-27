# 시간초과
# def solution(n):

#     answer = 0
    
#     for i in range(1,n+1) :
#         cnt = 0
#         for j in range(1,i+1) :
#             if(i % j == 0) :
#                 cnt +=1
#             if(cnt > 2) : break
            
#         if(cnt == 2) : answer +=1
    
#     return answer

#### 에라토스테네스의 체

import math

def solution(n):
    
    arr = [True] * (n+1)
    answer = 0
    
    for i in range(2,int(math.sqrt(n))+1):
        if arr[i] == False:
            continue
        
        for i in range(i+i, n+1, i):
            arr[i] = False
    for i in range(2, n+1):
        if arr[i] == True:
            answer += 1
            
    return answer