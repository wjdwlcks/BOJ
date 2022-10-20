
while 1:
    A = list(map(int, input().split()))
    Max = max(A)     
    if(Max==0):
        break    
    A.remove(Max)
    if  A[0]*A[0] + A[1]*A[1] == Max*Max:
        print('right')
    else:
        print('wrong')
