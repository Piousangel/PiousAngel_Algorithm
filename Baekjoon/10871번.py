import sys
x, y = map(int, sys.stdin.readline().split())

temp = list(map(int, sys.stdin.readline().split()))
    
for i in range(len(temp)) :
    if(temp[i] < y) :
        print(temp[i], end=' ')