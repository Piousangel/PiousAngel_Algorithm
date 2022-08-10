# 단어의 짝수번째 알파벳은 대문자, 홀수번째 알파벳은 소문자

def solution(s):
    answer = ''
    idx = 2
    
    for c in s :
        if c == ' ' :
            answer += c
            idx = 2
            continue

        if idx % 2 == 0 :
            answer += c.upper()
        else:
            answer += c.lower()
        idx += 1

    return answer