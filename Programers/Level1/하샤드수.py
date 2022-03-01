def solution(x):
    answer = True
    
    x_list = list(str(x))
    sum = 0
    for i in range(len(x_list)) :
        sum += int(x_list[i])

    if(x % sum == 0) : answer = True
    else : answer = False
    
    return answer


# def Harshad(n): # n은 하샤드 수 인가요? return n % sum([int(c) for c in str(n)]) == 0

