def solution(n):
    answer = 0
    
    str_list = list(str(n))
    
    for i in range(len(str_list)) :
        answer += int(str_list[i])

    return answer