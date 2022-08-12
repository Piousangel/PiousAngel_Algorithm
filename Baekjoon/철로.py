import sys
import heapq

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())
rail_list = []
heap = []
answer = 0


for i in range(n) :
    start, end = map(int, input().split())

    if start < end :
        rail_list.append( (start, end) )
    else:
        rail_list.append( (end, start) )

rail_list.sort(key = lambda x : (x[1], x[0]))

# print(rail_list)

railRoad = int(input())

for i in range(n) :
    now_start, now_end = rail_list[i][0], rail_list[i][1]
    
    if now_end - now_start > railRoad :
        continue

    if not heap :
        heapq.heappush(heap, (rail_list[i][0], rail_list[i][0]))
    else :
        while now_end - railRoad > heap[0][0] :
            heapq.heappop(heap)
            if not heap :
                break
        
        heapq.heappush(heap, (now_start, now_end))

    answer = max(answer, len(heap))

print(answer)

# for i in range(n) :
#     now_start, now_end = rail_list[i]

#     if now_end - now_start > road :
#         continue

#     if not rail_heap :
#         heapq.heappush(rail_heap, rail_list[i])
#     else:
#         while now_end - road > rail_heap[0][0] :
#             heapq.heappop(rail_heap)
#             if not rail_heap :
#                 break

#         heapq.heappush(rail_heap, (now_start, now_end))
    
#     answer = max(len(rail_heap), answer)

# print(answer)