# 파이썬 분할정복으로 구현
def quick_sort(arr, start, end):
    if start >= end: 
        return 

    left = start + 1
    right = end
    pivot = start 
    
    while left <= right:
        swap = 0
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            swap = arr[pivot]
            arr[pivot] = arr[right]
            arr[right] = swap

        else:
            swap = arr[right]
            arr[right] = arr[left]
            arr[left] = swap
           
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

arr  = [4,1,2,7,9,3,10,5,18,6]

print("before_arr", arr)
quick_sort(arr, 0, 9)
print("after_arr", arr)