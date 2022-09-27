N = int(input())
a = list(map(int, input().split()))
max =-1000000
min =1000000

for i in range(N):    
    if (a[i]>max):
        max=a[i]    
    if(a[i]<min):
        min=a[i]
        
print(min,max)


#N=int(input())
#array=list(map(int,input().split()))
#array.sort()
#print(array[0],array[-1])

#N=int(input())
#array=list(map(int,input().split()))
#print(min(array), max(array))