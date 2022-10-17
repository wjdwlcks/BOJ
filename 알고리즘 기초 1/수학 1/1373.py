print(oct(int(input(),2))[2:])

# 시간초과인 답인긴 한데 참고용
#
#from sys import stdin
#
#binary_List = list(map(int, stdin.readline().strip()))[::-1]
#total = 0
#res = []
#for i in range(len(binary_List)):
#    total += binary_List[i] * (2 ** i)
#
#while True:
#    if total == 0:
#        print(*res[::-1], sep='')
#        break
#    mok = total // 8
#    mod = total % 8
#    total = mok
#    res.append(mod)