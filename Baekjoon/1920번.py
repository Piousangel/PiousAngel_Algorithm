import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())

m_list = list(map(int, input().split()))

for m in m_list :
    start = 0
    end = len(n_list)-1
    mid = end // 2
    while end - start >= 0 :

        if m == n_list[mid] :
            print(1)
            break
        elif m > n_list[mid] :
            start = mid+1
        elif m < n_list[mid] :
            end = mid -1

        mid = (end+start)//2

    else:
        print(0)
    
    