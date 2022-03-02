from collections import deque

def solution(s):
    answer = True
    deq = deque()
    s_list = list(s)
    
    for i in range(len(s_list)) :
        if(len(deq) == 0) :
            if(s_list[i] == '(') :
                deq.append(s_list[i])
            else :
                return False
        else :
            if(deq.pop() == '(') :
                if(s_list[i] == '(') :
                    deq.append('(')
                    deq.append('(')
                else :
                    continue
    
    if(len(deq) == 0) : return True
    else : return False