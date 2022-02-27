def solution(n):
    
    # str1 = str(n)
    str_list = list(str(n))
    str_list.reverse()
    return list(map(int, str_list))

# def solution(n):
    
#     str_list = list(str(n))
#     str_list.reverse()
#     answer = [0 for i in range(len(str_list))]
#     for i in range(len(str_list)) :
#         answer[i] = int(str_list[i])
        
#     return answer