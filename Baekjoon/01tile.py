import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

arr = [0] * 1000001
arr[0] = 0
arr[1] = 1

cnt = 2

while cnt <= n :
    arr[cnt] = arr[cnt-1] + arr[cnt-2]
    cnt += 1

print(arr[n])