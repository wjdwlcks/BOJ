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
    

# N, K = map(int,input().split())
# ans= []
# arr = [i for i in range(1,N+1)] 
# num = 0
# for i in range(N):
#     num+=(K-1)
#     if num >= len(arr):
#         num %= len(arr)
#     ans.append(str(arr[num]))
#     arr.pop(num)

# print("<",', '.join(ans),">", sep="")