A,B,V = map(int,input().split())
cnt = (V-B)//(A-B)

if (V-B)%(A-B) > 0:
    cnt+=1

print(cnt)    

# import math

# A,B,V = map(int,input().split())

# day = (V-B)/(A-B)
# print(math.ceil(day))

#import math
#
#a, b, v = map(int, input().split())
#
#print(math.ceil((v-a)/(a-b)+1)) #올림함수 사용
