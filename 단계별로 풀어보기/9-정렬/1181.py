a=list()
for i in range(int(input())):
    
    word= input()
    wordlen = len(word)
    if [wordlen,word] not in a:
        a.append([wordlen,word])

a.sort(key=lambda x:(x[0],x[1]))

for i in a:
    print(*i[1],sep='')


#import sys
#
#n = int(sys.stdin.readline())
#lst = []
#
#for i in range(n):
#    lst.append(sys.stdin.readline().strip())
#set_lst = set(lst)
#lst = list(set_lst)
#lst.sort()
#lst.sort(key = len)
#
#for i in lst:
#    print(i)    