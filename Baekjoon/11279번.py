import heapq
import sys
n = int(sys.stdin.readline().rstrip())
heap = []
for i in range(n):
    inputN = int(sys.stdin.readline().rstrip())
    if inputN == 0 :
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-inputN, inputN))