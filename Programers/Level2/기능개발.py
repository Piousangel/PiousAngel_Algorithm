from collections import deque

def chkProcess(progresses, q):
    cnt = 0
    while q and progresses[q[0]] >= 100 :
        cnt +=1
        q.popleft()
        
    return cnt
    
def solution(progresses, speeds):
    answer = []
    q = deque()
    
    for i in range(len(progresses)):
        q.append(i)
    
    while q:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        temp = chkProcess(progresses, q)
        if temp > 0:
            answer.append(temp)
                
    return answer