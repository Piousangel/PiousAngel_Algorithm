n = int(input())

for i in range(n):
    a,b = map(int, input().split())
    total = 1
    for i in range(a):
        total *= b/a
        a -=1
        b -=1
    print((round(total)))