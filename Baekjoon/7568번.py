import sys

n = int(sys.stdin.readline().rstrip())

info = [[0 for _ in range(2)]for _ in range(n)]
rank = []
for i in range(n):
    kg, cm = map(int, sys.stdin.readline().split())
    info[i][0] = kg
    info[i][1] = cm

for i in range(n):
    cnt = 1
    for j in range(len(info)):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            cnt += 1
    print(cnt, end=' ')