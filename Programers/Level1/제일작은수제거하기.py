def solution(arr):
    answer = []
    a = min(arr)
    if len(arr) < 2 : return [-1]
    else : arr.remove(a)
    
    return arr