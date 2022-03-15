a, b = int(input().split())

def gcd(a,b):
    while b!= 0:
        temp = a%b
        a = b
        b = temp
    return abs(a)

c = b - a
d = b
k = gcd(c,d)
print(c//k +' '+ d//k)


