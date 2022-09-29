N = int(input())

C=1

while N>C:
    N=N-C
    C+=1
 
if C%2==0:
    print(f"{N}/{C+1-N}")
else:
    print(f"{C+1-N}/{N}")

#시간초과
#cnt=0
#idx=int(input())
#retcnt=0
#z=1
#while z:
#    cnt+=1   
#    front=0
#    back=0    
#    for j in range(1,cnt+1):
#        retcnt+=1
#        if (cnt%2==0):
#            back=(cnt+1)-j
#            front=j                                         
#        else:
#            front =(cnt+1)-j
#            back = j        
#        if(retcnt==idx):            
#            print(front,'/',back)
#            z=0
#            break      
        



            
        

