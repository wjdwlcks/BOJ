N= int(input())
# 1  7  19  37 61
# 6  12  18  24 
a = 6
cnt=1
while N>1:
    cnt+=1          
    N=N-a  
    a += 6  
        
print(cnt)    


## 다른 사람의 풀이
#n = int(input())
#room = 1
#cnt = 1
# 
#while n > room:
#    room = room + (6 * cnt)
#    cnt += 1
#print(cnt)