import sys
sys.setrecursionlimit(10**7)

def solution(word):
    answer = 0
    st = ''
    idx = 0
    target = 6
    
    alpha = ['A','E','I','O','U']
    # visited = [False] * len(alpha)
    str_list = []
    
    def dfs(st, idx, target) :
        
        if idx == target:
            return
        
        if st != '' :
            str_list.append(st)
        
        for i in range(0, len(alpha)) :
            dfs(st + alpha[i], idx+1, target)
    
    dfs(st, 0, target)
    
    answer = str_list.index(word) + 1
       
    return answer