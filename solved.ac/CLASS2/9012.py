a=[]
cnt1=0
cnt2=0
for i in range(int(input())):
    a = list(input())
    cnt1=0
    cnt2=0
    for i in a:
        if i == '(':
            cnt1+=1
        if i == ')':
            cnt2+=1
        if cnt1 < cnt2:            
            break
    if cnt1==cnt2:
        print('YES')
    else:
        print('NO')
        



#T = int(input())
#
#for i in range(T):
#    stack = []
#    a=input()
#    for j in a:
#        if j == '(':
#            stack.append(j)
#        elif j == ')':
#            if stack:
#                stack.pop()
#            else: # 스택에 괄호가 없을경우 NO
#                print("NO")
#                break
#    else: # break문으로 끊기지 않고 수행됬을경우 수행한다
#        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
#            print("YES")
#        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
#            print("NO")

#a = int(input())
#for i in range(a):
#    b = input()
#    s = list(b)
#    sum = 0
#    for i in s:
#        if i == '(':
#            sum += 1
#        elif i == ')':
#            sum -= 1
#        if sum < 0:
#            print('NO')
#            break
#    if sum > 0:
#        print('NO')
#    elif sum == 0:
#        print('YES')