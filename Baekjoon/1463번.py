n = int(input())
n_list = list(map(int, input().split()))
box = []

for i in range(n):
    box.insert(i-n_list[i], i+1)

for k in box:
    print(k, end=' ')

#insert 함수
# array.insert(i,x) 형태로 사용한다. 원하는 위치 i에 x를 삽입할 수 있다.
# 값 x는 객체로 추가, append함수와 마찬가지로 itereable자료형이더라도 하나의 요소로 삽입된다.