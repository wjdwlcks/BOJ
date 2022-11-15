from collections import deque

N,K = map(int, input().split())
L=deque()
for i in range(1,N+1): L.append(i)
res=[]

while L:
    for i in range(K-1):
        L.append(L.popleft())
    res.append(L.popleft())    


print(str(res).replace('[','<').replace(']','>'))