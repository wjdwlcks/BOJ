import sys
N=int(sys.stdin.readline())
a=list(map(int ,sys.stdin.readline().split()))
s= sorted(list(set(a)))
dic = {s[i] : i for i in range(len(s))}
#numdict = {}
#for i in range(len(a)):
#    numdict[a[i]] = i

for i in a:
    print(dic[i], end=' ')



  

        