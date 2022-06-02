import heapq
import math

def solution(n, works):
    answer = 0
    
    if sum(works) <= n :
        return 0
    
    heap = []
    
    for i in range(len(works)) :
        heapq.heappush(heap, (-works[i], works[i]))
        
    while n > 0 :
        
        temp = heapq.heappop(heap)[1]
        heapq.heappush(heap, (-temp + 1, temp - 1))
        n -= 1
        
    for i in range(len(heap)) :
        temp = math.pow(heapq.heappop(heap)[1], 2)
        answer += temp
    
    return answer