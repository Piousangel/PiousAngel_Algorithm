def solution(word):
    answer = 0
    
    aeiou = ['A','E','I','O','U']
    visited = [False] * 5
    arr = []
    def dfs(st, temp, idx) :
        
        if idx == 6 :
            return
        
        
        if st != '' :
            arr.append(st)
            
        for i in range(5) :
            dfs(st + temp[i], temp, idx+1)
          
    dfs('', aeiou, 0)
    
    answer = arr.index(word) +1
    
    return answer