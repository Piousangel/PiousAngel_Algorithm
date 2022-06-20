import sys
from itertools import combinations
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# 도시는 N개의 건물, M개의 도로
# 건물은 1번부터 N번까지 가지고 있음
# i 번째 도로는 A, B건물 사이를 1시간안에 양방향으로 이동가능한 도로
# 2개의 건물을 골라 치킨집 열려고 접근성의 합이 최소화 
# 건물 x의 접근성은 x에서 가장 가까운 치킨집까지 왕복하는 최단 시간


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)

house = []
for i in range(1, N+1) :
    house.append(i)

# print(house)

arr = [0,0]

for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def chkCost(idx, graph, temp_list, visited2) :

    q = deque()

    q.append([idx, 0])
    visited2[idx] = True

    while q :

        now, cost = q.popleft()

        if now in temp_list :
            break

        for node in graph[now] :
            if visited2[node] != True :
                visited2[node] = True
                q.append([node, cost+1])
    
    return cost

def chkDistance(graph, arr) :

    global answer_list

    temp = 0
    

    for i in range(1, N+1) :
        visited2 = [False] * (N+1)
        if i != arr[0] and i != arr[1] :
            temp += chkCost(i, graph, arr, visited2)

    if answer_list[2] > temp :
        answer_list[2] = temp
        answer_list[0] = arr[0]
        answer_list[1] = arr[1]

# def dfs(house, arr, idx, visited, graph) :

#     if idx == len(arr) :
#         chkDistance(graph, arr)
#         return

#     for i in range(len(house)) :
#         if visited[i] != True :
#             visited[i] = True
#             arr[idx] = house[i]
#             dfs(house, arr, idx+1, visited, graph)
#             visited[i] = False


answer_list = [0, 0, sys.maxsize]

con = list(combinations(house, 2))

for t in con :
    chkDistance(graph, t)

answer_list[2] *= 2

print(answer_list)