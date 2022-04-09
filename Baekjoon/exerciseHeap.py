import heapq

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)

print(heap)

#원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴
print(heapq.heappop(heap))
print(heap)
print("==============")
print(heapq.heappop(heap))
print(heap)
print("==============")
print(heap[0])
print("==============")
# 여기서 주의사항은 인덱스 0에 가장 작은 원소가 있다고 해서, 인덱스 1에 두번째 작은 원소, 인덱스 2에 세번째 작은 원소가 있다는 보장은 없다는 것입니다. 
# 왜냐하면 힙은 heappop() 함수를 호출하여 원소를 삭제할 때마다 이진 트리의 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문입니다.
# 따라서 두번째로 작은 원소를 얻으려면 바로 heap[1]으로 접근하면 안되고, 
# 반드시 heappop()을 통해 가장 작은 원소를 삭제 후에 heap[0]를 통해 새로운 최소값에 접근해야 합니다.

#기존 리스트를 힙으로 변환
heap = [4,1,7,3,8,5]
heapq.heapify(heap)
print(heap)


# 최대 힙 만들기는 힙에 튜플을 원소로 추가하거나, 삭제하면, 튜플내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리
# 따라서 최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, 구조의 튜플을 힙에 추가하거나 삭제하면 된다.
# 그리고 힙에서 값을 읽어올 때는 각 튜플에서 인덱스+1 값을 가져오면 된다.
print()
numbers = [4,1,7,3,8,5]
print(numbers)

tempHeap = []

for num in numbers:
    heapq.heappush(tempHeap, (-num, num))

while heap:
    print(heapq.heappop(tempHeap)[1])