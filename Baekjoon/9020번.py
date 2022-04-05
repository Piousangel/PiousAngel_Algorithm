








# n = 8
#     visited = [False] * (n+1)
#     temp = int((n+1)**0.5)             #    (n+1) 의 **5 한것의 배수만 찾으면 된다고 함.
    
#     for i in range(2, temp+1):         #절반까지만 어차피 배수 찾을 거라 배수 아닌 것들은 다 소수
#         if visited[i] == False:
#             for j in range(i+i, n+1, i):
#                 visited[j] = True
    
#     for i in range(2, len(visited)):
#         if visited[i] == False:
#             print(i)