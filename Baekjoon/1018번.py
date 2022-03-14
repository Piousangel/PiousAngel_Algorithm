#귀찮은 문제 같아요.. 다시

import sys

row, col = map(int, sys.stdin.readline().split())

board = []

for i in range(row):
    board.append(sys.stdin.readline().rstrip())

for i in range(row):
    str1 = sys.stdin.readline().rstrip()
    for j in range(0, len(str1)):
        if str1[0] == 'W':
            print("re")