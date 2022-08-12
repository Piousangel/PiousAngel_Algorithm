# number 리스트 안 숫자로 target 만들어
# 더하기, 빼기만 가능
answer = 0

def solution(numbers, target):
    
    global answer
    idx = 0
    total = 0
    visited = [False] * len(numbers)
    
    def dfs(total, idx, target) :
        global answer 
        if idx == len(numbers) :
            if total == target :
                answer += 1
            return
        
        dfs(total + numbers[idx], idx +1, target)
        dfs(total - numbers[idx], idx +1, target)
    
    dfs(total, idx, target)
    
    return answer