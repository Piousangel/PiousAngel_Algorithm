import math

def solution(n, s):
    answer = []
    k = s
    total = 1
    if n > s :
        return [-1]
    while n > 0 :
        
        temp = math.ceil(s/n)
        answer.append(temp)
        s -= temp
        n -= 1
        
    # if total < k :
    #     return [-1]
    # else :
    answer.sort()
    return answer