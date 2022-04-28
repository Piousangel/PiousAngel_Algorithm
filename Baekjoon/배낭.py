import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

# 배낭에 들어있거나 없거나

arr = [ [0] * (K+1) for _ in range(N+1) ]
n_list = [[0,0]]

for i in range(N):
    weight, value = map(int, input().split())
    n_list.append([weight, value])

for i in range(1, len(arr)):
    for j in range(1, len(arr[0])):
        weight = n_list[i][0]
        value = n_list[i][1]

        if j < weight :              #
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j-weight]+ value, arr[i-1][j])
    
print(arr[N][K])