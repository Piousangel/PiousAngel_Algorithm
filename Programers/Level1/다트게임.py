import math
from collections import deque

def solution(dartResult):
    answer = 0
    idx = 0
    number = ''
    n_list = ['S', 'D', 'T']
    q = deque()
    
    flag = False
    
    for i in range(len(dartResult)) :
        
        if dartResult[i] in n_list :
            if len(q) < 2 :
                q.append(math.pow(int(number), n_list.index(dartResult[i])+1))
                number = ''
            else :
                answer += q.popleft()
                q.append(math.pow(int(number), n_list.index(dartResult[i])+1))
                number = ''
                
        elif dartResult[i] == '*' :
            flag = True
            number = ''
            
            while q :
                now = q.popleft()
            
                if len(q) == 0 :
                    q.append(now*2)
                    break
                else :
                    answer += now * 2
        
        elif dartResult[i] == '#' :
            flag = True
            number = ''
            
            while q :
                now = q.popleft()
                print(now)
                if len(q) == 0 :
                    q.append(now * (-1))
                    break
                else:
                    answer += now
        else :
            number += dartResult[i]
          
    while q :
        temp = q.popleft()
        answer += temp
                  
    return answer