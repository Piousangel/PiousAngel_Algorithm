import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

for i in range(n) :
    coin_cnt = int(input())  #몇개 코인 들어오는지
    coin_list = map(int, input().split())
    target = int(input())

    arr = [0] * (target+1)
    arr[0] = 1
    
    for coin in coin_list :
        for j in range(0, target+1) :
            
            if j >= coin :
                arr[j] += arr[j-coin]

    print(arr[target])