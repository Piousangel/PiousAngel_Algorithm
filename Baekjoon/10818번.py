import sys

c = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))

print(min(n_list), end=' ')
print(max(n_list), end=' ')