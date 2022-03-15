n,r = map(int, input().split())

arr = list(range(1,n+1))
box = [0]*r

def showBox(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()
            
def dfs(arr, box, start, idx, r):
    if(idx == r):
        showBox(box)
        return
    
    for i in range(start, len(arr)):  
        box[idx] = arr[i]
        dfs(arr, box, i, idx+1, r)
     
dfs(arr, box, 0, 0, r)