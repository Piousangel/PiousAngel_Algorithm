import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    num, str1 = sys.stdin.readline().split()
    for ch in str1:
        print(ch*int(num), end='')
    print()

# import sys

# n = int(sys.stdin.readline())

# for i in range(0, n+1):
#     num, str1 = map(str, sys.stdin.readline().split(" "))
#     for ch in str1:
#         for j in range(0, int(num)+1):
#             print(ch, end="")
#     print()