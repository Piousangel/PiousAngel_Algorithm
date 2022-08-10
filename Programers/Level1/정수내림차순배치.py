def solution(n):
    
    answer = 0
    temp = ''
    
    strN = str(n)
    n_list = list(map(int, strN.rstrip()))
    
    n_list.sort(reverse = True)
    
    for k in n_list :
        temp += str(k)
    
    answer = int(temp)
    return answer