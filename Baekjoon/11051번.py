n, k = map(int, input().split())

def binary(n,k):
    if k == 0 or k == n:
        return 1
    result = binary(n-1,k) + binary(n-1,k-1)
    return result
      
temp = binary(n,k)
print(temp%10007)