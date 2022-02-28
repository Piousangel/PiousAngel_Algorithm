import copy

def solution(strings, n):
    answer = []
    
    for i in range(len(strings)) :
        strings[i] = strings[i][n] + strings[i]
    
    strings.sort()
    
    for i in range(len(strings)) :
        answer.append(strings[i][1:])
    
    # answer = copy.copy(strings)
    return answer