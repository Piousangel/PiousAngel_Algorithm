import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
arr = [ 0 for _ in range(n+1)]

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    arr[b] += 1

answer = []
def top_sort() :
    q = deque()
    global answer
    for i in range(1, len(arr)) :
        if arr[i] == 0 :
            q.append(i)

    while q :
        
        now_node = q.popleft()
        answer.append(now_node)

        for node in graph[now_node] :
            arr[node] -=1

            if arr[node] == 0 :
                q.append(node)

top_sort()


for i in answer :
    print(i, end= ' ')
