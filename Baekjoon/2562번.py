import sys
cnt = 1
maxN = 0
po = 0

while True:
    try:
        num = int(sys.stdin.readline())
        if(num > maxN) :
            maxN = num
            po = cnt
        cnt = cnt +1
    except:
        break

print(maxN)
print(po)