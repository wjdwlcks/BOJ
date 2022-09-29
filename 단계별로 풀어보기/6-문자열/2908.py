a, b =  map(int, input().split())

A = (a%10)*100 +((a%100)//10)*10 + (a%1000)//100
B = (b%10)*100 + ((b%100)//10)*10  + (b%1000)//100

if A>B:
    print(A)
else:
    print(B)

#a, b = input().split()
#a = a[::-1]
#b = b[::-1]
#print(max(a, b))