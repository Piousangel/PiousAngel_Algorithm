import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

answer = []
def bfs(k) :
    global answer
    q = deque()
    for i in range(1, n+1):
        q.append(i)
    idx = 1
    while q :

        now = q.popleft()

        if idx == k :
            answer.append(now)
            idx = 1
        else:
            q.append(now)
            idx += 1


bfs(k)

print("<", end= "")
for i in range(len(answer)) :
    if i != len(answer) -1 :
        print(answer[i], end = ", ")
    else:
        print(answer[i],end = ">")
    