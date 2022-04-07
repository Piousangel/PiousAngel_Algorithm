
#최소성, 유일성 만족  겹치는 것들 중에서 str로 더해서 딕셔너리에 다르게 들어가면 후보키?
def solution(relation):
    answer = 0
    
    dictionary = {}
    for i in range(len(relation[0])):
        dictionary[i] = []
        
    for i in range(len(relation)):
        for j in range(len(relation[0])):
           
            dictionary[j].append(relation[i][j])
    
    print(dictionary)
    
    for i in range(len(dictionary)):
        if len(set(dictionary[i])) == len(dictionary[i]):  #하나 찾음
            answer += 1
            del dictionary[i]
    print("=====")        
    print(dictionary)
    return answer