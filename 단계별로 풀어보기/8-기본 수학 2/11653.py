cnt=0
N=int(input())
i=2
while N!=1:
    if(N%i==0):
        N=N//i    
        print(i)
    else:
        i+=1

#import math
#target_num = int(input())
#dive_num = int(math.sqrt(target_num))
#
#each_dive = 2
#
#while each_dive <= dive_num :
#    if target_num % each_dive == 0 :
#        target_num = target_num // each_dive
#        print(each_dive)
#        each_dive = 2
#    
#    else : 
#        each_dive += 1
#
#if target_num > 1 : 
#    print(target_num)        


#import sys
#input = sys.stdin.readline
#n = int(input())
#for i in range(2, int(n ** 0.5) + 1): # 제곱근보다 작은 범위
#    if n % i == 0:
#        while n % i == 0:
#            n //= i
#            print(i)
#if n > 1:
#    print(n)