import sys
num = int(sys.stdin.readline())

for i in range(1, num+1) :
    for j in range(num-i) :
        print(" " , end='')
    for k in range(0,i) :
        print("*", end='')
    print()