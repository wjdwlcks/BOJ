def gcd(A,B):    
    while B>0:
        A,B= B , A%B
    return A

for i in range(int(input())):
    A,B= map(int,input().split())
    print(A*B//gcd(A,B))
    



#import sys
#import math
#input = sys.stdin.readline
#
#t = int(input())
#
#for i in range(t):
#    a, b = map(int, input().split())
#    l = math.lcm(a, b)##최소공배수
#    print(l)