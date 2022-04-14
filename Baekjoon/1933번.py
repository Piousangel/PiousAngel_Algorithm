import sys
import heapq

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

tower_info = []

# tower_info.append( (0,0,0) )    #결국 x y로 비교하고 높이를 우선순위 큐에 넣어줘서 큐 길이 구하는거같은데
x_info_heap = []
y_info_heap = []
h_info_heap = []

for i in range(n):
    left, h, right = map(int, input().split())

    tower_info.append((left, right, h))

# print(tower_info)
tower_info.sort(key = lambda x : (x[1], x[0]))
print(tower_info)

for i in range(len(tower_info)):

    if len(info_heap) == 0 :
        # heapq.heappush(info_heap, tower_info[i])

    else:
        # heap_temp = heapq.heappop(info_heap)
        # heap_x = heap_temp[0]
        # heap_y = heap_temp[1]
        # heap_h = heap_temp[2]
        # print(heap_x, heap_y, heap_h)
        # temp = tower_info[i]
        # now_x = temp[0]
        # now_y = temp[1]
        # now_h = temp[2]
        # print(now_x, now_y, now_h)
        # print("======================")
        # heapq.heappush(info_heap, tower_info[i])
