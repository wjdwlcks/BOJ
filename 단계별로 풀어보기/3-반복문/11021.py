import sys
a= int(input())

for i in range(1,a+1):
    a,b = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {a+b}")

#n = int(input()) 
#for i in range(n): 
#    a, b = map(int, input().split()) 
#    print("Case #%s: %s" % (i+1,a+b))    
