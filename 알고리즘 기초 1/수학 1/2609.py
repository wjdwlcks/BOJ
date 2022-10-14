def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a,b = map(int,input().split())

max= gcd(a,b)
# for i in range(1,10001):
#     if a%i==0 and b%i==0:
#         max = i
print(max)        
print(a*b//max)

