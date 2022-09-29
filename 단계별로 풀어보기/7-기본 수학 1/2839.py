N = int(input())

cnt=0

while 1:
    if(N==0):
        print(cnt)
        break
    if((N%5==0 or N%5==3 ) and N-5>=0):
        cnt+=1
        N=N-5
        continue
    elif((N%3==5 or N%3==2 or N%3==0 or N%3==1) and N-3>=0):
        cnt+=1
        N=N-3
        continue
    else:
        print(-1)
        break

#
#num = int(input())
#count = 0
#
#while num >= 0:
#  if num % 5 == 0:
#    count += int(num // 5)
#    print(count)
#    break
#  
#  num -= 3
#  count += 1
#  
#else:
#  print(-1)    
#


    
    


