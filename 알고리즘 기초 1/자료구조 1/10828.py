import sys
class Stack:
    def push(list,X):
        list.append(X)   

    def pop(list):      
        if len(list) == 0:
            print(-1)
        else:    
            print(list.pop())
             
    def size(list):                
        print(len(list))

    def empty(list):
        if len(list) == 0:
            print(1)
        else:
            print(0)

    def top(list):      
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])

list = []
for i in range(int(input())):
    cmd = sys.stdin.readline().split()
    if cmd[0]=='push':
        Stack.push(list,cmd[1])
    elif cmd[0]=='pop':    
        Stack.pop(list)    
    elif cmd[0]=='size':      
        Stack.size(list)          
    elif cmd[0]=='empty':                
        Stack.empty(list)
    elif cmd[0]=='top':    
        Stack.top(list)            



#import sys
#
#N = int(sys.stdin.readline())
#
#stack = []
#
#for _ in range(N) :
#    word = sys.stdin.readline().split() #입력 받는데 split해서 입력 받기
#    order = word[0] #명령어 받기
#    
#    #order의 값에 따라 역할을 수행하기
#    
#    #order가 push라면
#    if order =="push" :
#        value = word[1]
#        stack.append(value)
#    
#    #order가 pop이라면
#    elif order=="pop" :
#        if len(stack)==0 :
#            print(-1)
#        else :
#            print(stack.pop())
#    
#    #order가 size라면
#    elif order=="size" :
#        print(len(stack))
#    
#    #order가 empty라면
#    elif order=="empty" :
#        if len(stack)==0 :
#            print(1)
#        else : 
#            print(0)
#    
#    #order가 top이라면
#    elif order=="top" : 
#        if len(stack)==0 : 
#            print(-1)
#        else : 
#            print(stack[-1])
