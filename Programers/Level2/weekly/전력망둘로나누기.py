from collections import deque


def chkWires(wires, idx):
    q = deque()
    arrList = []
    cnt = 0
    for arr in wires :
        arrList.append(arr)
        
    q.append(arrList[idx][1])
    arrList.pop(idx)
    
    while q:
        
        wireNum = q.popleft()
        for i in range(0, len(arrList)):
            
            flag = False
            temp = arrList[i]
            
            if wireNum == temp[0] :
                flag = True
                q.append(temp[1])
                arrList.remove(temp)
                # cnt += 1
                
            elif wireNum == temp[1] :
                flag = True
                q.append(temp[0])
                arrList.remove(temp)
                # cnt += 1
            
            if flag:
                i -= 1
        cnt += 1
    return cnt
        
    return answer

def solution(n, wires):
    answer = 1001
    
    for i in range(len(wires)):
        leftWire = chkWires(wires, i)
        rightWire = n - leftWire
        
        temp = abs(leftWire - rightWire)
        answer = min(answer, temp)
        
    return answer