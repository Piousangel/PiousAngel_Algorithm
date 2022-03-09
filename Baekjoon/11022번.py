import sys
num = int(sys.stdin.readline())
cnt = 1
# for i in range(num) :
#     x, y = map(int, sys.stdin.readline().split())
#     print("Case #"+str(cnt)+": "+str(x)+" + " + str(y) + " = " + str(x+y))
#     cnt = cnt +1

for i in range(1,num+1) :
    x, y = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {x} + {y} = {x+y}')