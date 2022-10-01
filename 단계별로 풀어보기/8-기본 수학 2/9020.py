N = 10001
isPrime = [True] * N
isPrime[1] = False

for i in range(2, int(N**0.5)+1):
    if isPrime[i]:
        for j in range(2*i, N, i):
            isPrime[j] = False

for i in range(int(input())):
    P=int(input())
    S1=0
    S2=0
    M=10000
    for j in range(1,P+1):
        if isPrime[j]:
            if isPrime[P-j] :  
                if(P-j-j >= 0):
                    if(P-j-j < M):
                        S1=j
                        S2=P-j
                    M=P-j-j                    
                else:
                    continue                                                                                        
    print(S1,S2)                                
                


#def is_prime(n):
#    if n == 1:
#        return False
#    for j in range(2, int(n**0.5) + 1):
#        if n % j == 0:
#            return False
#    return True
#
#
#for _ in range(int(input())):
#    num = int(input())
#
#    a, b = num//2, num//2
#    while a > 0:
#        if is_prime(a) and is_prime(b):
#            print(a, b)
#        else:
#            a -= 1
#            b += 1    





#sosu = [0 for i in range(10001)]
#sosu[1] = 1
#for i in range(2, 98):
#    for j in range(i * 2, 10001, i):
#        sosu[j] = 1
#t = int(input())
#for i in range(t):
#    a = int(input())
#    b = a // 2
#    for j in range(b, 1, -1):
#        if sosu[a - j] == 0 and sosu[j] == 0:
#            print(j, a - j)
#            break
