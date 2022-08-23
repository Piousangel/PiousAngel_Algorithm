import sys
from collections import deque

sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())


q = deque()

for i in range(1, n+1) :
    q.append(i)

while len(q) > 1:

    now = q.popleft()

    if len(q) == 1 :
        break
    else:
        q.append(q.popleft())
        

print(q.popleft())
    