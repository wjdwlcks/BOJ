input()
N = list(map(int,input().split()))
sum = 0
for i in N:
    cnt=0
    for j in range(2,i+1):
        if(i%j==0):
            cnt+=1
    if(cnt==1):
        sum+=1
print(sum)


#n = int(input())
#numbers = map(int, input().split())
#sosu = 0
#for num in numbers:
#    error = 0
#    if num > 1 :
#        for i in range(2, num):  # 2부터 n-1까지
#            if num % i == 0:
#                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
#        if error == 0:
#            sosu += 1  # error가 없으면 소수.
#print(sosu)