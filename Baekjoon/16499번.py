import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

str_list = []

for i in range(n):
    str_list.append(input().rstrip())

if str_list[1][0] in str_list[2] :
    print("a")
else:
    print("b")