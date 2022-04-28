# import sys
# sys.stdin = open('sample.txt')
# input = sys.stdin.readline

# str1 = input().rstrip()
# str2 = input().rstrip()


# arr = [ [0] * (len(str2)+1) for _ in range( len(str1)+1 ) ]

# for i in range(1, len(str1)+1):
#     for j in range(1, len(str2)+1):
#         if str1[i-1] == str2[j-1] :
#             arr[i][j] = arr[i-1][j-1] + 1
#         else:
#             arr[i][j] = max(arr[i][j-1], arr[i-1][j])

# print(arr[-1][-1])

import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

arr = [ [0]* (len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str[j-1] :
            arr[i][j] = arr[i-1][j-1] +1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
            
print(arr[-1][-1])