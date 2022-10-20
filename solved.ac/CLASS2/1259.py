from audioop import reverse


while 1:
    word=input()
    if(word=='0'): break 
    if(word ==  "".join(reversed(word))): # word[::-1]
        print('yes')
    else:
        print('no')
    




#num = input()
#while num != '0':
#    isPalindrome = 1
#    for i in range(len(num) // 2):
#        if num[i] == num[len(num) - (i+1)]:
#            continue
#        else:
#            isPalindrome = 0
#            break
#            
#    if isPalindrome:
#        print('yes')
#    else:
#        print('no')
#    num = input()