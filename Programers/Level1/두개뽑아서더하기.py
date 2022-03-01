def solution(numbers):
    answer = []
    
    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            tmp = numbers[i] + numbers[j]
            if(i != j and answer.count(tmp) == 0) :
                answer.append(tmp)
   
    answer.sort()
    return answer