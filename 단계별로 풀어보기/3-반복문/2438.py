a=int(input())
for i in range(a):
    for j in range(i+1):
        print('*' ,end='')
    print()

# 1
# [print('*' * i) for i in range(1, int(input())+1)]

#2
#n = int(input())
#
#for i in range(1, n+1):  # 1부터 n까지
#    print('*' * i)
