import heapq
def solution(A, B):
    answer = 0
    
    heapq.heapify(A)
    heapq.heapify(B)
    
    while len(B) != 0 :
        
        tempA = heapq.heappop(A)
        tempB = heapq.heappop(B)
        
        if tempB <= tempA :
            heapq.heappush(A, tempA)
        else:
            answer += 1
    
    return answer