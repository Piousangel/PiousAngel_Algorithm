def solution(phone_number):
    answer = ''
    
    star = len(phone_number[:-4])
    temp = phone_number[-4:]
    
    answer = "*" * star
    answer = answer + temp
    
    return answer