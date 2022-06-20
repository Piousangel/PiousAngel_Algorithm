import sys
sys.setrecursionlimit(10**7)

def solution(word):
    answer = 0
    char_list = ['A','E','I','O','U']
    
    temp_list = []
    
    def dfs(s, temp_list, char_list) :
        
        if len(s) == len(char_list) :
            temp_list.append(s)
            return
        
        if s != '' :
            temp_list.append(s)
               
        for ch in char_list :
            dfs(s+ch, temp_list, char_list)
    
    dfs('', temp_list, char_list)
    # print(temp_list)
    answer = temp_list.index(word)
    return answer+1