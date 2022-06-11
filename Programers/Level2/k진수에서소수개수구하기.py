import math

def solution(n, k):
    answer = 0
    reverse = ''
    
    while n > 0 :
        n, temp = divmod(n, k)
        reverse += str(temp)
        
    temp_str = reverse[::-1]
    
    str_list = list(temp_str.split('0'))
    
    for ch in str_list :
        
        if ch == '' or ch == '1' :
            continue
        
        strToNum = int(ch)
        
        for i in range(2, int(math.sqrt(strToNum))+1) :
            if strToNum % i == 0 :
                break
        else :
            answer += 1
                
    return answer