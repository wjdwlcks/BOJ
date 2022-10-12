from operator import truediv


a=list()
max = 0
for i in input():
    a.append(i)

a.sort(reverse=True)
print(*a,sep='')    
      
#print(''.join(reversed(sorted(input()))))    