import sys

def solution(arr):
    
    minNum = sys.maxsize
    
    if len(arr) == 1 :
        return [-1]
    else:
        for k in arr :
            if minNum > k :
                minNum = k
                
    arr.remove(minNum)
    return arr