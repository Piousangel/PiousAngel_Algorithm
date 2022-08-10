def solution(n):
    
    answer = []
    
    strN = str(n)
    
    n_list = list(map(int, strN.rstrip()))
    n_list.reverse()
    
    return n_list