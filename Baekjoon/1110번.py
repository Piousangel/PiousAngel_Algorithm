import sys

num = int(sys.stdin.readline())
temp = num
cnt = 0
flag = True
while flag:
    a = temp // 10
    b = temp % 10
    c = (a+b) % 10
    temp = (b*10) + c
    cnt = cnt + 1
    if temp == num :
        flag = False

print(cnt)