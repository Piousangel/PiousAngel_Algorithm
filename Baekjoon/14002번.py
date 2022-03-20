n = int(input())

arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
max_dp = max(dp)
print(max_dp)

max_idx = dp.index(max_dp)
answer_list = []
while max_idx >=0:
    if max_dp == dp[max_idx]:
        answer_list.append(arr[max_idx])
        max_dp -=1
    max_idx -= 1
    
answer_list.reverse()
print(*answer_list)