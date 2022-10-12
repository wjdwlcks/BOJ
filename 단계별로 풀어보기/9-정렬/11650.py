import sys
a=[]
input=sys.stdin.readline
for i in range(int(input())):
    a.append(list(map(int,input().split())))    

a.sort(key=lambda x:(x[0],x[1]))

for i in a:
    print(*i)


#N=int(input())
#arr=[]
#for i in range(N):
#    a,b = map(int,input().split())
#    arr.append((a,b))
#arr.sort()
#for i in range(N):
#    print(arr[i][0],arr[i][1])