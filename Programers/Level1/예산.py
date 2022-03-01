def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    
    for i in range(len(d)) :
        if(budget >= d[i]) :
            sum += d[i]
            budget -= d[i]
            answer += 1
        else : break