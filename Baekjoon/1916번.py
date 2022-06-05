import sys
import heapq
input = sys.stdin.readline
maxValue = sys.maxsize

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
arr = [maxValue] * (N+1)               # 출발점에서 시작해서 도착지로 가는 cost 최소가 나올 때 마다 계속 갱신해줘요!

for i in range(M):
    A, B, cost = map(int, input().split())
    graph[A].append((B, cost))

start_num, end_num = map(int, input().split())

# 만약 3번지점이라고 하면 어떻게 오던 나(3번)한테 오기까지 cost가 낮은 것으로 갱신하면 된다.
def bfs(graph, arr, start_num) :

    q = []
    arr[start_num] = 0
    heapq.heappush(q, (0, start_num))

    while q :

        now_cost, pos = heapq.heappop(q)
        
        if arr[pos] < now_cost:
            continue
            
        for node in graph[pos] :
            cost = now_cost + node[1]

            if arr[node[0]] > cost :
                arr[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

bfs(graph, arr, start_num)
print(arr[end_num])