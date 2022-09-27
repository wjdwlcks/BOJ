N = int(input())

for i in range(N):
    a = list(input())
    cnt=0    
    tempcnt=0    
    for i in a:                
        temp=i        
        if(temp=='O'):
            tempcnt += 1
            cnt+=tempcnt
        else:
            tempcnt = 0            
    print(cnt)
                            

