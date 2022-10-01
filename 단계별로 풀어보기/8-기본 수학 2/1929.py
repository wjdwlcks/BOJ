x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1: #1은 소수가 아뉘지!
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)

#
#m, n = map(int, input().split())
#
#prime = [True] * 1000001
#prime[1] = False
#
#for i in range(2, 1000001):
#    if i ** 2 > 10000001:
#        break
#
#    if prime[i]:
#        for j in range(i + i, 1000001, i):
#            prime[j] = False
#
#for i in range(m, n + 1):
#    if prime[i]:
#        print(i)        