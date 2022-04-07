n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start+end) // 2

    if arr[mid] == target :
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

result = binary_search(arr, target, 0, n-1)
if result is None:
    print('찾을 수 없습니다.')
else:
    print(result+1)