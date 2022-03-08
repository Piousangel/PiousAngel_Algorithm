import sys  
num = int(sys.stdin.readline())

for x in range(num) :
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)