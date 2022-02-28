def solution(arr):
    answer = []
    a = 11
    for i in range(len(arr)) :
        if(a != arr[i]) :
            answer.append(arr[i])
        a = arr[i]
    
    return answer