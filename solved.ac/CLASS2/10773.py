import sys
res=[]
for i in range(int(input())):
    K = int(sys.stdin.readline())
    if(K==0):
        res.pop()
    else:
        res.append(K)

print(sum(res))