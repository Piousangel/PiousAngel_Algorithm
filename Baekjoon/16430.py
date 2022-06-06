import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

a, b = map(int, input().split())

temp = b - a
k1 = 0
k2 = 0
for i in (2, temp+1) :
    if temp % i == 0 and b % i == 0 :
        temp = temp // i
        b = b // i

print(temp, b)