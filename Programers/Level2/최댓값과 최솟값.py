def solution(s):
    answer = ''
    num_list = s.split(" ")
    max_n = 0
    min_n = 0
    box = []
    
    for i in range(len(num_list)) :
        box.append(int(num_list[i]))
    # box.sort()
    # print(box)
    answer += str(min(box)) + " "+ str(max(box))
    return answer