def solution(numbers, target):
    global answer
    total = 0
    dfs(numbers, target, total, 0)
    
    return answer

answer = 0
def dfs(arr, target, total, idx):
    global answer
    if idx == len(arr):
        if total == target:
            answer += 1
        return

    total += arr[idx]
    dfs(arr, target, total, idx+1)
    total -= arr[idx]
    total -= arr[idx]
    dfs(arr,target, total, idx+1)
    
    
    