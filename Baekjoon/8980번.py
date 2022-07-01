import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

# 조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
# 조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
# 조건 3: 박스들 중 일부만 배송할 수도 있다.

# 트럭 한 대로 배송할 수 있는 최대 박스 수는?
# 받는 마을번호는 보내는 마을번호보다 항상 크다

# 트럭 용량이 40이고 보내는 박스들이 다음표와 같다
# 
N, C = map(int, input().split())

n = int(input())

arr = []

for i in range(n) :
    # give, take, boxNum = map(int, input().split())
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x : x[1]) #도착지 기준 정렬

box = [C]*(N+1)
answer = 0
for give, take, boxNum in arr :
    minNum = C

    for i in range(give, take) :
        minNum = min(minNum, box[i])
    
    minNum = min(minNum, boxNum)

    for i in range(give, take) :
        box[i] -= minNum
    
    answer += minNum

print(answer)
