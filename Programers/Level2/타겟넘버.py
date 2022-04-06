def dfs(numbers, idx, total, target):
    global answer
    if idx == len(numbers):
        # print(total)
        if total == target:
            answer += 1
        return
            
    dfs(numbers, idx+1, total + numbers[idx], target)
    dfs(numbers, idx+1, total - numbers[idx], target)
    
    
answer = 0
def solution(numbers, target):
    
    dfs(numbers, 0, 0, target)
    return answer
    
# def solution(numbers, target):
#     global answer
#     total = 0
#     dfs(numbers, target, total, 0)
    
#     return answer

# answer = 0
# def dfs(arr, target, total, idx):
#     global answer
#     if idx == len(arr):
#         if total == target:
#             answer += 1
#         return

#     total += arr[idx]
#     dfs(arr, target, total, idx+1)
#     total -= arr[idx]
#     total -= arr[idx]
#     dfs(arr,target, total, idx+1)
    
    
    