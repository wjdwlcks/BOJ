#h,m,p = map(int, input().split())
h,m= map(int, input().split())

p= int(input())

if(h+(m+p)//60 >23 ):
    print( (h+(m+p)//60)%24, (m+p)%60)
else : 
    print(h+(m+p)//60, (m+p)%60)
        

#H, M = map(int, input().split())
#timer = int(input()) 
#
#H += timer // 60
#M += timer % 60
#
#if M >= 60:
#    H += 1
#    M -= 60
#if H >= 24:
#    H -= 24
#
#print(H,M)
