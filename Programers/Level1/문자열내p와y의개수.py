def solution(s):
    answer = True
    # box = ['p','y']
    
    s = s.lower()
    
    str_list = list(s)
    pCnt = 0
    yCnt = 0
    
    for i in range(len(str_list)) :
        if(str_list[i] == "p") :
            pCnt += 1
        elif(str_list[i] == "y") :
            yCnt += 1

    if(pCnt == yCnt) : return True
    else : return False