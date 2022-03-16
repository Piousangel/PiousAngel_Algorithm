n = int(input())

def p_info(start, end):
    print(start, end, sep=" ")
    
def hanoi(n, start, end, mid):
    if n == 1:
        p_info(start, end)
    else:
        hanoi(n-1, start, mid, end)
        p_info(start, end)
        hanoi(n-1, mid, end, start)
        
print(2**n-1)
if(n <=20):
    hanoi(n,1,3,2)
# n = int(input())
# n_list = []
# cnt = 0
# def p_info(start, end):
#     global cnt
#     global n_list
#     temp_list = []
#     temp_list.append(start)
#     temp_list.append(end)
#     n_list.append(temp_list)
#     cnt += 1
        
# def hanoi(n, start, end, mid):
#     if n == 1:
#         p_info(start, end)
#     else:
#         hanoi(n-1, start, mid, end)
#         p_info(start, end)
#         hanoi(n-1, mid, end, start)

# hanoi(n,1,3,2)

# print(cnt)
# if cnt <= 20 :
#     for c_list in n_list:
#         print(c_list[0], c_list[1])