a=list(map(int,input().split()))
sum=0
for i in a:
    sum+= i*i # i**2

print(sum%10)

#print(sum([n**2 for n in map(int, input().split())]) % 10)