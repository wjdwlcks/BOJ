
import sys

input = sys.stdin.readline

inputList = list()

N = 123456*2 + 1
isPrime = [True] * N

for i in range(2, int(N**0.5)+1):
    if isPrime[i]:
        for j in range(2*i, N, i):
            isPrime[j] = False


def counting(inputValue):
    cnt = 0
    for k in range(inputValue+1, inputValue*2 + 1):
        if isPrime[k]:
            cnt += 1
    print(cnt)


while True:
    k = int(input())

    if not k:
        break
    counting(k)
#출처: https://tooo1.tistory.com/564 [개발자 퉁이리:티스토리]


# while 1:
#     N=int(input())
#     cnt=0
#     if(N==0):
#         break
#     for i in range(N,2*N+1 ):
#         if i == 1: #1은 소수가 아뉘지!
#             continue
#         if i==2:
#             cnt+=1
#             continue
#         if i%2==0:
#             continue
#         for j in range(2, int(i** 0.5)+1 ):
#             if i%j==0:
#                 break
#         else:
#             cnt+=1
#     print(cnt)            