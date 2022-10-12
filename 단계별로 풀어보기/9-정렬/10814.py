import sys
a= list()
for i in range(int(sys.stdin.readline())):
    age,name = sys.stdin.readline().strip().split()    
    a.append([int(age),name,i])


a.sort(key=lambda x:(x[0],x[-1]) )
for i in a:
    print(i[0],i[1])


#import sys
#n = int(sys.stdin.readline())
#member = []
#for i in range(n):
#    member.append(list(sys.stdin.readline().split()))
#member.sort(key=lambda x: int(x[0]))
#for i in range(n):
#    print(member[i][0], member[i][1])    