K,N = map(int, input().split())
A = []
C=[]

for  _ in range(K):
    A.append(int(input()))

l = 1
r = 2147483648

while 1:
    count = 0
    mid = (l+r)//2
    for i in A:
        count += i//mid
    if r-1 <= l:
        break
    if count < N:
        r = mid
    else:
        l = mid
print(l)        


    


    



    