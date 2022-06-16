#복습하기

def solution(word):
    
    alph_list = ['A', 'E', 'I', 'O', 'U']
    blank = ''
    arr = []
    cnt = 0
    
    def dfs(word, cnt) :
        
        if len(word) > len(alph_list) :
            return
        
        if word != blank :
            arr.append(word)
        
        for ch in alph_list :
            dfs(word+ch, cnt + 1)

    dfs(blank, 0)
    return arr.index(word)+1
    