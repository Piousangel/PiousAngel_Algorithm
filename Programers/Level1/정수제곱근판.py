import sys
import math

def solution(n):
    answer = 0
    
    temp = math.sqrt(n)
    tempInt = int(temp)
    
    if int(tempInt) * int(tempInt) == n :
        answer = (tempInt+1) * (tempInt+1)
    else :
        answer = -1
    
    return answer
