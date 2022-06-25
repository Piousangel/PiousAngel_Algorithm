import heapq
def solution(jobs):
    idx = 0
    total = 0
    start = 0
    now = 1
    heap = []
    
    while idx < len(jobs) :
        
        for i in range(idx, len(jobs)) :
            if start <= jobs[i][0] < now :
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
                
        if len(heap) > 0 :
            temp = heapq.heappop(heap)
            start = now
            now += temp[0]
            total += now - temp[1]
            idx += 1
        else:
            now += 1
            
    return total // len(jobs)