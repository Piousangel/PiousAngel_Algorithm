# skill은 선행스킬이 있음
# skill_trees에서 올바른 스킬구성을 가진 것이 몇개 있는지 찾아라

def solution(skill, skill_trees):
    
    answer = 0
    
    for sk in skill_trees :
        
        idx = 0
        flag = True
        for ch in sk :
            if ch in skill :
                if skill.index(ch) == idx :
                    idx += 1
                    continue
                else :
                    flag = False
                    break
            else:
                continue
                
        if flag == True :
            answer += 1
        
    return answer