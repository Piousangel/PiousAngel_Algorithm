def solution(s):
    answer = ''
    tmp = ''
    cnt = 0
    s = s.lower()
    # print(s)
    
    for i in range(len(s)) :
        if(s[i] == ' ') :
            cnt = 0
            answer += ' '
            continue
        if(cnt == 0) :
            if('a' <= s[i] and s[i] <= 'z') :
                answer += s[i].upper()
                cnt += 1
            else :
                cnt +=1
                answer += s[i]
        else :
            answer += s[i]
            cnt += 1
    
    return answer