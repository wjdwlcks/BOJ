for i in range(int(input())):
    a= list(input().split())
    for j in a:
        print(''.join(reversed(j)), end = ' ')
    print()
    

#import sys
#
#n = int(sys.stdin.readline())
#
#for _ in range(n):
#  words = sys.stdin.readline().rstrip().split()
#
#  for word in words:
#    print(word[::-1], end=' ')
#  print()


#N=int(input())
#
#for i in range(N):
#    string=input()
#    string+=" "
#    stack=[]
#    for j in string:
#        if j!=" ":
#            stack.append(j)
#        else:
#            while stack:
#                print(stack.pop(), end='')
#            print(' ', end='')