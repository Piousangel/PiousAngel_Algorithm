import heapq

# nums = [4,1,7,3,8,5]
# heap = []

# for num in nums:
#     heapq.heappush(heap, (-num, num))

# while heap:
#     print(heapq.heappop(heap)) # index 1

# K번째 최소값/최대값

# def kth_smallest(nums, k):
#     heap = []
#     for num in nums:
#         heapq.heappush(heap, num)

#     kth_min = None
#     for i in range(k):
#         kth_min = heapq.heappop(heap)
#     return ktth_min

# print(kth_smallest([4,1,7,3,8,5], 3))

# 힙 정렬

def heap_sort(nums):
    heap = []
    for num in nums :
        heapq.heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

print(heap_sort([4,1,7,8,5]))
