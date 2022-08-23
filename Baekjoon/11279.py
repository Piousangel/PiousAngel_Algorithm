import sys
import heapq
sys.stdin = open('sample.txt')

input = sys.stdin.readline
heap = []
n = int(input())

# x라면 배열에 넣고, 0이라면 가장 큰 값 출력

for i in range(n) :
    temp = int(input())
    if temp == 0 :
        if len(heap) == 0 :
            print("0")
        else:
            k = heapq.heappop(heap)
            print(k[1])
    else:
        heapq.heappush(heap, (-temp, temp))
