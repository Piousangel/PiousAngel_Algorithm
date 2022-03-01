def solution(n):
    answer = 0
    one_cnt = 0
    t_list = list(bin(n)[2:])
    for i in range(len(t_list)) :
        if(t_list[i] == '1') :
            one_cnt += 1
            
    while True :
        n += 1
        one_c = 0
        a_list = list(bin(n)[2:])
        for i in range(len(a_list)) :
            if(a_list[i] == '1') :
                one_c += 1
            if(one_c > one_cnt) : break
        if(one_cnt == one_c) :
            answer = n
            break
        
    return answer