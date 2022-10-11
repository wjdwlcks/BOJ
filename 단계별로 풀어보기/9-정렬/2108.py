a=list()
N = int(input())
for i in range(N):
    a.append(int(input()))

a.sort()

print(sum(a)//N)
print(a[N//2])
print(max(a)-min(a))


