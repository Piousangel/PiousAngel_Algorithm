import sys

num = int(sys.stdin.readline())
answer = 0
                
for i in range(1, num+1):
    if len(str(i)) < 3 :
        answer += 1
    else :
        n_list = list(map(int, str(i)))
        if n_list[0] - n_list[1] == n_list[1] - n_list[2]:
            answer +=1
                
print(answer)