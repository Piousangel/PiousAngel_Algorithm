#내일 다시
def solution(n, times):
    answer = 0
    
    times.sort()
    leftT = 0
    rightT = times[len(times)-1] * n
    
    while leftT <= rightT:
        
        midT = (rightT + leftT) // 2
        total = 0
        for i in range(len(times)):
            total += midT // times[i]
            
        if total < n :        #사람을 더 받아야 하면 작은 시간을 플러스 해줘야
            leftT = midT + 1
        else:
            rightT = midT - 1
            answer = midT
    
    return answer