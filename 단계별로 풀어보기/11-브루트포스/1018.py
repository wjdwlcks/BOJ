N,M = map(int, input().split())
a=[]
ret=[]
for j in range(N):
    a.append(input())

for i in range(N-7):
    for z in range(M-7):
        cnt1=0
        cnt2=0             
        for j in range(i,i+8):    
            for k in range(z,z+8):            
                    if j%2==0 and k%2==0:
                        if a[j][k] != 'W':
                            cnt1+=1
                    elif j%2==0 and k%2==1:                
                        if a[j][k] != 'B':
                            cnt1+=1                
                    if j%2==1 and k%2==0:
                        if a[j][k] != 'B':
                            cnt1+=1
                    elif j%2==1 and k%2==1:                     
                        if a[j][k] != 'W':
                            cnt1+=1                    
                    if j%2==0 and k%2==0:
                        if a[j][k] != 'B':
                            cnt2+=1
                    elif j%2==0 and k%2==1:                
                        if a[j][k] != 'W':
                            cnt2+=1                    
                    if j%2==1 and k%2==0:
                        if a[j][k] != 'W':
                            cnt2+=1
                    elif j%2==1 and k%2==1:                     
                        if a[j][k] != 'B':
                            cnt2+=1
        ret.append(cnt1) 
        ret.append(cnt2)                             
print(min(ret))



#N,M = map(int, input().split())
#a=[]
#ret=[]
#for j in range(N):
#    a.append(input())
#
#for i in range(N-7):
#    for z in range(M-7):
#        cnt1=0
#        cnt2=0             
#        for j in range(i,i+8):    
#            for k in range(z,z+8):
#                if (j+k)%2==0:
#                    if a[j][k] != 'W':
#                        cnt1+=1
#                    else:   
#                        cnt2+=1                 
#                else:
#                    if a[j][k] != 'B':
#                            cnt1+=1      
#                    else:
#                        cnt2+=1                                                                                                                          
#        ret.append(cnt1) 
#        ret.append(cnt2)                             
#print(min(ret))




