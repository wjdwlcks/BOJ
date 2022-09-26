x = int(input())
y = int(input())

if (x < 0):
    if(y < 0):
        print('3')
    else:
        print('2')        
elif (x > 0):
    if(y < 0):
        print('4')   
    else:
        print('1')     

#x = int(input())
#y = int(input())
#if x > 0:
#	print(1 if y > 0 else 4)
#else:
#	print(2 if y > 0 else 3)        