def solution(s):
    answer = ''
    
    if(len(s) % 2 == 0) :
        answer = s[len(s)//2-1 : len(s)//2+1]
    else :
        answer = s[len(s)//2 : len(s)//2+1]
        
    return answer


    # int/int 는 float 형으로 출력된다. 따라서 // 로 계산해줘야함