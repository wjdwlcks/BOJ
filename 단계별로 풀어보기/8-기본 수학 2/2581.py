a= int(input())
b= int(input())
sum = 0
min = 10000

for i in range(a,b+1):    
    cnt=0
    for j in range(2,i+1):
        if i%j==0:
            cnt+=1
    if(cnt==1):        
        sum+=i
        if(min>i):
            min=i

if sum>0:
    print(sum)
    print(min)                                                
else:
    print(-1)   
    
#
#start_num = int(input())
#last_num = int(input())
#
#sosu_list = []
#for num in range(start_num, last_num+1):
#    error = 0
#    if num > 1 :
#        for i in range(2, num):  # 2부터 num-1까지
#            if num % i == 0:
#                error += 1
#                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
#        if error == 0:
#            sosu_list.append(num)  # error가 없으면 소수리스트에 추가
#            
#if len(sosu_list) > 0 :
#    print(sum(sosu_list))
#    print(min(sosu_list))
#else:
#    print(-1)
#
#


