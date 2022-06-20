def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
    temp = 0
    for i in range(2, n+1, 2) :
        dp[i] = (dp[i-2] * 3) % 1000000007 + (temp * 2) % 1000000007
        temp += dp[i-2]
        
    
    return dp[n] % 1000000007