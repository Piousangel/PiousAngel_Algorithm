#재귀로 푸니까 런타임 에러가 나오네용?

def dfs(s, s_length, idx, cnt):
    global answer
    if cnt == s_length-1:
        if len(s) == 0:
            answer = 1
        else:
            
            if s[0] == s[1]:
                answer = 1
            else:
                answer = 0
        return
    
    else:
        temp = ""
        if s[idx] == s[idx+1]:
            temp = s[0:idx] + s[idx+2: ]
            dfs(temp, s_length, 0, cnt+2)
        else:
            dfs(s, s_length, idx+1, cnt+1)
    
answer = 0
def solution(s):
    global answer
    dfs(s, len(s), 0, 0)
    return answer