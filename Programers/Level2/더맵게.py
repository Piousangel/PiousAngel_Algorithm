from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville) #최소힙(이진트리형식)
    
    while(scoville[0] < K and len(scoville) > 1) : # while 범위 좀만더 생각
        c1 = heappop(scoville)
        c2 = heappop(scoville)
        heappush(scoville, c1 + (c2*2))
        answer += 1
        
    return answer if scoville[0] >= K else -1

# from collections import deque
# def solution(scoville, K):
#     answer = 0
#     q = deque()
#     for tmp in scoville :
#         if(tmp < K) :
#             q.append(tmp)
    
#     while(q.popleft() < K) :
#         ki = q.popleft() + (q.popleft()*2)
#         if(ki < K) :
#             q.append(ki)
#             answer += 1
    
#     return answer


