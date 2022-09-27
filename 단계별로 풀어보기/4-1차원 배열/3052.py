a = [] 

for i in range(10):
    b = int(input())
    a.append(b%42) 

print(len(set(a)))

#1

#arr = []
#for i in range(10):
#    a = int(input())
#    if a%42 not in arr:
#        arr.append(a % 42)
#print(len(arr))

#2

#a=set()
#
#for i in range(10):
#    a.add(int(input())%42)
#
#print(len(a))