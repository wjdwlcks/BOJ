h,m = map(int, input().split())

if(m>44):
    print(h, m-45)
elif(h>0 and m<45):
    print(23 , m+15 )
else:
    print(23,m+15)

    
#a, b = map(int, input().split())
#
#A = a*60+b-45
#
#if (A<0):
#    print(23, 60+A)
#else:
#    print(A//60, A%60)
