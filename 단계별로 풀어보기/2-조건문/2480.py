f,s,t = map(int, input().split())

if(f==s==t):
    print(10000+f*1000)
elif(f==s or s==t):    
    print(1000+s*100)
elif (f==t):
    print(1000+f*100)
else :
    print(100*max(f,s,t))



#arr = list(map(int, input().split()))
#temp = 0
# 
#if len(set(arr)) == 1:   # 3개가 동일한 경우
#    print((10**4) + (arr[0] * 1000))
# 
#elif len(set(arr)) == 3:    # 모두 다른 경우
#    print(max(arr) * 100)
# 
#else:    # 2개가 동일한 경우
#    for i in range(3):
#        if arr.count(arr[i]) == 2:
#            temp = arr[arr.index(arr[i])]
#    print(1000 + (temp * 100))