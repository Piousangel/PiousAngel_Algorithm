n = int(input())
n_list = list(map(int, input().split()))
dic = {}

for i in range(1, n+1):
    dic[i] = n_list[i-1]
    
arr = [i for i in range(1,n+1)]
answer = 0

def printf(box, dic):
    sumA = 0
    sumB = 0
    global answer
    for i in box:
        sumA += i
        if sumA > n:
            break
        sumB += dic.get(i)
    if sumA == n:
        answer = max(answer, sumB)

def dfs(arr, box, dic, start, idx, r):
    if idx == r:
        printf(box, dic)
        return
        
    for i in range(start, len(arr)):
        box[idx] = arr[i]
        dfs(arr, box, dic, i, idx+1, r)
            
for i in range(1, n+1):
    box = [0] * i
    dfs(arr, box, dic, 0, 0, i)
    
print(answer)