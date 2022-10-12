import sys
a=[]
input=sys.stdin.readline
for i in range(int(input())):
    a.append(list(map(int,input().split())))    

a.sort(key=lambda x:(x[1],x[0]))

for i in a:
    print(*i)