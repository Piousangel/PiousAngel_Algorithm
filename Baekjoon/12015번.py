import bisect

n = int(input())
    
arr = map(int, input().split())

dp = [arr[0]]
    
for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
   
print(len(dp))

#bisect.bisect_left(arr, x): arr가 정렬되어있다는 가정하에 x값이 들어갈 위치 반환
# 현재 위치(i)가 이전 위치의 원소보다 작거나 같으면, bisect.bisect_left로 이전 위치의 원소 중 가장 큰 원소의 idx값 구함 dp의 idx 원소를 arr[i]로 바꿔준다.
#O(NlogN)