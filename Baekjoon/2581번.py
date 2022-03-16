start = int(input())
end = int(input())
total = 0
minN = 100001 
for i in range(start, end+1):
    flag = True
    if i > 1:
        for j in range(2,i):
            if(i%j == 0):
                flag = False
                break
        if flag:
            total += i
            minN = min(minN, i)
if total == 0:
    print(-1)
else:
    print(total)
    print(minN)