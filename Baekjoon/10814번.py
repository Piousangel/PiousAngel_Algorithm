from collections import deque

n = int(input())
info = [[0 for _ in range(2)] for _ in range(n)]

q = deque()
for i in range(n):
    age, name = map(input().split())
    q.append((age,name))

while q:
    nowAge, nowName = q.popleft()
    flag = True
    for age, name in q:
        if nowAge < age:
            flag = False
            break
    if flag == True:
        print(f'{nowAge} {nowName}')
    else:
        q.append((nowAge, nowName))