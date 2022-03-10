import sys
a = int(sys.stdin.readline())
n = list(sys.stdin.readline().strip())
sum = 0
for i in n:
    sum += int(i)
print(sum)