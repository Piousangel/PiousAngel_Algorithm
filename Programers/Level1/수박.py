def solution(n):
    box = ['수','박']
    answer = ''
    
    for i in range(n) :
        answer += box[i%2]
    
    return answer