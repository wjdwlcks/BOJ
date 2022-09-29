for i in range(int(input())):
    N, string = input().split()
    for j in string:
        for k in range(int(N)):            
            print(j, end='')
    print('')

#n = int(input())
#
#for _ in range(n):
#    cnt, word = input().split()
#    for x in word:
#        print(x*int(cnt), end='')  # end='' 옆으로 붙임
#    print()  # 줄넘김    
            