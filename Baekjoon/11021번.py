import sys
num = int(sys.stdin.readline())
case = 1
for i in range(num) :
    x, y = map(int, sys.stdin.readline().split())
    print("Case #"+str(case)+": "+str(x+y))
    case = case+1