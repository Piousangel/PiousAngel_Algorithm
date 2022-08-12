import heapq
import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n) :
    k = int(input())
    
    if k == 0 :
        if len(heap) == 0 :
            print(0)
            continue
        print(heapq.heappop(heap)[1])
    else :
        heapq.heappush(heap, [-k, k])



