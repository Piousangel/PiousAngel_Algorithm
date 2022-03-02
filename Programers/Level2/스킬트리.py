def solution(skill, skill_trees):
    answer = 0
    s_list = list(skill)

    for str in skill_trees :
        flag = True
        cnt = 0
        # print(len(skill))
        for ch in str :
            # print(ch)
            if cnt == len(s_list) - 1 :
                flag = True
                break
                
            if ch in skill :
                if(ch == s_list[cnt]) :
                    cnt +=1
                    continue
                else :
                    flag = False
                    break
            else :
                continue
                
        if flag == True : answer +=1

    return answer