import sys
n= int(input())

for i in range(1,n+1):
    a,b = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {a} + {b} = {a+b}")


#case = int(input())
#for i in range(case):
#    a, b = map(int, input().split())
#    print('Case #%d: %d + %d = %d' %(i+1, a, b, a+b))