def solution(phone_number):
    answer = ''
    
    str = phone_number[-4:]
    str2 = phone_number[0:-4]
    
    for i in range(len(str2)) :
        answer += "*"
    
    answer += str
    return answer