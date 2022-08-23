import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline
stack = []

n = int(input())

for i in range(n) :
    num = int(input())

    if num == 0 :
        stack.pop(-1)
    else :
        stack.append(num)

print(sum(stack))