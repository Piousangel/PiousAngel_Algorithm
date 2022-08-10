import sys

def solution(x):
    
    answer = True
    
    strN = str(x)
    temp = list(strN.rstrip())
    total = 0
    
    for i in range(len(temp)) :
        total += int(temp[i])
        
    if int(x) % total == 0 :
        answer = True
    else:
        answer = False
    
    return answer