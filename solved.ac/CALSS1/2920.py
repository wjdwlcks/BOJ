a=list(map(int,input().split()))
status=0
for i in range(len(a)-1):
    if a[i]-a[i+1] == 1:
        status+=1
    elif a[i]-a[i+1] == -1:
        status-=1

if status==-7:
    print('ascending')
elif status==7:
    print('descending')
else:
    print('mixed')

#a = list(map(int, input().split()))
# 
#if a == sorted(a):
#    print('ascending')
#elif a == sorted(a, reverse=True):
#    print('descending')
#else:
#    print('mixed')    
    

