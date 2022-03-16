import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0
num = 1
while True:
    if num > n :
        break
    n = n - num
    num += 1
    cnt += 1

print(cnt)