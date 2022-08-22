def solution(word):
    answer = 0
    
    alpha = ['A','E','I','O','U']
    arr = []
    
    def dfs(st, alpha, idx) :
    
        if idx == 6 :
            return 
        
        if st != '' :
            arr.append(st)
            
        for i in range(len(alpha)) :
            dfs(st + alpha[i], alpha, idx + 1)
    
    dfs('', alpha, 0)
    
    answer = arr.index(word) + 1
    return answer