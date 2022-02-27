def solution(s):
    answer = ''
    
    str_list = list(s)
    cnt = 2
    for i in range(len(str_list)) :
        if(str_list[i] == ' ') :
            cnt = 2
            answer += str_list[i]
            continue
        elif(cnt % 2 == 0) :
            answer += str_list[i].upper()
        else :
            answer += str_list[i].lower()
        
        cnt +=1
        
    return answer