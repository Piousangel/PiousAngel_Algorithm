import math
def solution(n):
    answer = 0
    
    a = int(math.sqrt(n))

    if a * a == n : return (a+1)*(a+1)
    else : return -1