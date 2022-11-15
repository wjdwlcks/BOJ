from collections import deque

for i in range(int(input())):
    N,M= map(int,input().split())
    L=deque()
    a=list(map(int,input().split()))
    for i in a:        
        L.append(i)
    cnt=0
    while L:
        for i in list(L):
            if max(L)>i:
                L.append(L.popleft())
            else:
                L.popleft()
                cnt +=1
    print(cnt)
            

