a,b = map(int, input().split())
total = 0

for i in range(a,b+1):
    num = 1
    cnt = 0
    while i>=1:
        i = i - num
        num += 1
        cnt += 1
            
    total += cnt
print(total)