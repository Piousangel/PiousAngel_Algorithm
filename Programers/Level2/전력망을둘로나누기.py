from collections import deque     #다시
import copy

def chkWire(wires, idx):
    cnt = 0
    w_list = copy.deepcopy(wires)
    # w_list = []
    
    # for i in range(len(wires)):
    #     w_list.append(wires[i])
        
    q = deque()
    q.append(w_list[idx][1])
    # w_list.remove(idx)
    del w_list[idx]
  
    while q:
        
        temp = q.popleft()
        
        for i in range(0, len(w_list)):
            flag = False
            
            if temp == w_list[i][0]:
                flag = True
                q.append(w_list[i][1])
                w_list.remove(w_list[i])
                
               
            elif temp == w_list[i][1]:
                flag = True
                q.append(w_list[i][0])
                w_list.remove(w_list[i])
                              
            if flag:
                i -= 1
        
        cnt +=1
        
    return cnt

def solution(n, wires):
    answer = 0
    minValue = 1001
    print(wires)
    for i in range(len(wires)):
        
        leftWire = chkWire(wires, i)
        rightWire = n - leftWire
        print(leftWire, rightWire)
        minValue = min(minValue, abs(leftWire- rightWire))
        
    return minValue