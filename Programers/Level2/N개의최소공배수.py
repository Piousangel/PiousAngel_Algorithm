from fractions import gcd

def solution(num):      
    answer = num[0]
    
    for i in num:
        answer = i * answer / gcd(i, answer)
        # print(answer)

    return answer