a=''
int(input())
a=input()
hash = 0

for i in range(len(a)):
    hash+=(int(ord(a[i]))-96) * (31 ** i )

print(hash%1234567891)    