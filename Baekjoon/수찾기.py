import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))
# print(n_list)
# print(m_list)
for i in m_list:
 
    left = 0
    right = len(n_list) -1
    mid = 0

    while left <= right :
        mid = (left + right) // 2

        if i == n_list[mid] :
            print("1")
            break
        if i  < n_list[mid] :
            right = mid -1
        elif i > n_list[mid] :
            left = mid +1
    else:
        print("0")
