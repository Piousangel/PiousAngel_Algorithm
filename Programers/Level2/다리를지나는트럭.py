from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_sum = 0
    q = deque()
    
    for tr_weight in truck_weights:
        
        while True :
            if not q:
                q.append(tr_weight)
                answer+=1
                total_sum = tr_weight
                break
            else:
                if len(q) == bridge_length:
                    total_sum -= q.popleft()
                    
                elif total_sum + tr_weight <= weight :
                    total_sum += tr_weight
                    answer += 1
                    q.append(tr_weight)
                    break
                else:
                    # print("아아아")
                    q.append(0)         # 0을 넣어서 q크기를 맞춰주는 거군요 .......
                    answer += 1
    # print(q)
    return answer + bridge_length