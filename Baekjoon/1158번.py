from collections import deque

a, b = map(int, input().split())
cnt = 1
n_list = []
q = deque()

for i in range(1,a+1):
    q.append(i)

while q:
    temp = q.popleft()
    if cnt == b:
        n_list.append(str(temp))
        cnt = 0
    else:
        q.append(temp)
    cnt +=1
    
print("<",", ".join(n_list)[:],">", sep='')