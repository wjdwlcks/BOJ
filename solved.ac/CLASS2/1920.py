import sys
sys.stdin.readline()
A= list(map(int,sys.stdin.readline().split()))
sys.stdin.readline()
B= list(map(int,sys.stdin.readline().split()))

set(A)
A.sort()

for i in  B:
    mid = len(A)//2 
    while 1 :
        
        if (mid == 0 or mid== len(A)-1) and i != A[mid]:
            sys.stdout.write('0\n')
            break   

        if i < A[mid]:     
            mid = mid//2
        elif i > A[mid]:       
            mid = (len(A)+mid)//2
        else:
            sys.stdout.write('1\n')
            break
    sys.stdout.write('0\n')   