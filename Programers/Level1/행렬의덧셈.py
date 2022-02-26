def solution(arr1, arr2):
    # answer =  [[] for x in range(len(arr2))]
    
    # answer = [arr1[i] + arr2[i] for i in range(len(arr1))]
    # [list1[i] + list2[i] for i in range(len(list1))]
    
    # for i in arr1, arr2:
    #     for j in i:
    #         # print(j, end=' ')
    #         answer = arr1[j] + arr2[j]
    # print()
    
#     for i in range(len(arr1)):
        
#         for j in range(len(arr1[i])):
#             arr1[i][j] += arr2[i][j]
    answer = [[arr1[i][j]+arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

    # zip 함수 사용하기 [x+y for x,y in zip(list1, list2)]
    # answer = [[c+d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]
    return answer