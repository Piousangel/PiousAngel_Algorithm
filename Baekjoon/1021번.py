import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, m = map(int, input().split())    
n_list = list(map(int, input().split()))  
q = deque()

for i in range(1, n+1) :
    q.append(i)

cnt = 0

for num in n_list :
    while True :
        if q[0] == num :
            q.popleft()
            break
        else:
            if q.index(num) < len(q)/2 :  # len(q)//2 하면 안됨
                while q[0] != num :
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != num :
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)

