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
hanoi(n,1,3,2)