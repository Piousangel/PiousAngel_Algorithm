import heapq
import sys
n = int(sys.stdin.readline())
heap = []   
for i in range(n):
    inputN = int(sys.stdin.readline())
    if inputN == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, inputN)

#heapq 힙
#기존 리스트를 힙으로 변환
# n_list = [4,3,5,1,2]
# heapq.heeapify(n_list)
# print(n_list)
# -> [1,2,3,4,5]
