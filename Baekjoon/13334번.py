import sys
import heapq

sys.stdin = open('sample.txt')
input = sys.stdin.readline

answer = 0
n = int(input())

rail_list = []
rail_heap = []

for i in range(n) :
    a, b = map(int, input().split())
    if a < b :
        rail_list.append([a,b])
    else:
        rail_list.append([b,a])

road = int(input())

rail_list.sort(key = lambda x : (x[1], x[0]))    # 도착지점을 기준 오름차순 정렬

print(rail_list)


# 매 상황마다 가능한 사람들의 왼쪽 시작점을 담아 두는 우선순위 큐
# 매번 돌때마다 그림에서 포함되는 선분 갯수는 우선순위 큐의 크기와 동일합니다.
# 따라서 최댓값을 갱신할 때는 웃선순위 큐의 크기를 가지고 하면 됩니다.

for i in range(n) :
    now_start, now_end = rail_list[i]

    if now_end - now_start > road :
        continue

    if not rail_heap :
        heapq.heappush(rail_heap, rail_list[i])
    else:
        while now_end - road > rail_heap[0][0] :
            heapq.heappop(rail_heap)
            if not rail_heap :
                break

        heapq.heappush(rail_heap, (now_start, now_end))
    
    answer = max(len(rail_heap), answer)

print(answer)



# while now_end - rail_heap[0][0] > road :
#             heapq.heappop(rail_heap)
#             if not rail_heap :
#                 break