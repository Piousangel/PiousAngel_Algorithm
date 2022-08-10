def solution(s, n):
    
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
             'r','s','t','u','v','w','x','y','z']
    
    answer = ''
    isUpper = False
    
    for c in s :
        if c == ' ' :
            answer += c
            continue
        
        if c.lower() != c : # 원래 소문자
            isUpper = True
        else:
            isUpper = False
        
        idx = (alpha.index(c.lower()) + n) % 26
        
        if isUpper == True :
            answer += alpha[idx].upper()
        else :
            answer += alpha[idx]
        
    return answer