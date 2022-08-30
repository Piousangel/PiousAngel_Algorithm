def solution(clothes):
    answer = 1
    
    dic = {}
    
    for i in range(len(clothes)):    #의상 이름은 생각할 필요가 없어요.
        if clothes[i][1] not in dic:
            dic[clothes[i][1]] = 1
        else:
            dic[clothes[i][1]] += 1
  
    for i in dic.values():
        answer *= i+1
   
    return answer -1