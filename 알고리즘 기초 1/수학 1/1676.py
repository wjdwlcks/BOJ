def factorial(N):
    if N < 2:
        return N
    else:
        return N * factorial(N-1)

res=0
a= factorial(int(input()))
while 1 :    
    if a%10 == 0 and a!=0:
        res+=1
        a=a//10
    else:
        break        
print(res)   
        

