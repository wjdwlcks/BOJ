N = int(input())
ret = 0
for i in range(1,N):
    sum = i
    A=i    
    while A>0:
        sum+=A%10 
        A=A//10
    if(sum == N):
        ret = i
        break

print(ret)    

#N = int(input()) #1
#result = 0 #2
#for i in range(1, N+1) :  
#    A = list(map(int, str(i))) #3
#    result = i + sum(A) #4
#    if result == N : #5
#        print(i)
#        break
#
#    if i==N: #6
#        print(0)
#


# N = int(input())
# n=N
# cnt = 0
# min = 0
# # 몇 자리 숫자인지 구하기
# while True:
#     if n/10 < 1:
#         cnt +=1
#         break
#     else:
#         cnt += 1
#         n=n/10
# # 어디부터 어디까지 돌릴지 정함
# t=0
# if N-9*cnt >0:
#     t = N-9*cnt
# for i in range(t,N+1):
#     k=i
#     tot=i
#     for j in range(0,cnt,1):
#         tot+= int(k%10)
#         k= int(k/10)
#     if tot == N:
#         min=i
#         break

# print(min)


