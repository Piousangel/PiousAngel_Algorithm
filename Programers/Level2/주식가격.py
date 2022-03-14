from collections import deque

def solution(prices):
    answer = []
    q = deque()
    
    for x in prices:
        q.append(x)
        
    while q :
        temp = q.popleft()
        cnt = 0
        for s in q:
            cnt += 1      
            if s < temp:
                break   
        answer.append(cnt)    
                
    return answer