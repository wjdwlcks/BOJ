N= int(input())
cnt = 0 
N0 = N
while 1 :
    cnt+=1    
    N10= N0//10 
    N1= N0%10
    N0 = N1*10 + (N1+N10)%10       
    if(N0 == N):
        break    
        
print(cnt)
#1

#N = input()
#if int(N) < 10:
#    N = "0" + N
#
#calNum = N[1] + str(int(N[0]) + int(N[1]))[-1]
#count = 1
#
#while calNum != N:
#    calNum = calNum[1] + str(int(calNum[0]) + int(calNum[1]))[-1]
#    count += 1
#
#print(count)

#2

#N = int(input())
#new_N = N
#cnt = 0
#
#while True:
#    new_N = (new_N % 10) * 10 + (new_N // 10 + new_N % 10) % 10
#    cnt += 1
#    if new_N == N:
#        break
#
#print(cnt)