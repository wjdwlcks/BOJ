N = int(input())
cnt = 0

for i in range(1,N+1):
    if i<100 :
        cnt+=1
    elif i<1000:
        H=i        
        D=[]
        while H:
            D.append(H%10)
            H=H//10                        
        if( D[2]- D[1] == D[1]-D[0]):                         
            cnt+=1
            
print(cnt)            

            
    

               
#n = int(input())
#hansu = 0
#
#for i in range(1, n + 1):
#    if i < 100:             # 1부터 99까지는 모두 한수
#        hansu += 1
#    else:                   # 100부터는, ex) 123 -> 3 - 2 =  2 - 1
#        n_str = list(map(int, str(i)))
#        if n_str[2] - n_str[1] == n_str[1] - n_str[0]:
#            hansu += 1
#
#print(hansu)            



#1) 100 미만의 자연수는 모두 조건에 해당한다. 즉 100보다 작을 때는 입력을 그대로 출력하면 된다.
#
#2) 1000은 해당하지 않으므로 세 자리 자연수만 신경쓰면 된다.
#
#3) 세 자리 자연수는 가운데 숫자*3이 각 자리 숫자의 합이면 조건에 해당한다.
#
# 
#
#n = int(input())
#if n < 100:
#    print(n)
#else:
#    cnt = 99
#    for i in range(100, n+1):
#        if int(str(i)[1]) * 3 == sum(map(int, list(str(i)))):
#            cnt += 1
#    print(cnt)

