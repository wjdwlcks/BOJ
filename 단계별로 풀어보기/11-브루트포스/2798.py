N,M = map(int,input().split())

a = list(map(int, input().split()))
ret = 0
for i in range(N):
    sum=a[i]
    for j in range(N):
        if i==j:
            continue
        for k in range(N):                        
            if j==k or k==i:
                continue
            if(sum+a[j]+a[k]) <= M:
                if ret < sum+a[j]+a[k]:
                    ret = sum+a[j]+a[k]                           
print(ret)                


#N, M = map(int, input().split())
#arr = list(map(int, input().split()))
#result = 0
#for i in range(N):
#   for j in range(i+1, N):
#       for k in range(j+1, N):
#           if arr[i] + arr[j] + arr[k] > M:
#               continue
#           else:
#               result = max(result, arr[i]+arr[j]+arr[k])
#print(result)


#from itertools import combinations
#
#card_num, target_num = map(int, input().split())
#card_list = list(map(int, input().split())
#biggest_num = 0
#
#for cards in combinations(card_list, 3):
#   temp_sum = sum(cards)
#   if biggest_sum < temp_sum <= target_sum:
#       biggest_sum = temp_sum
#print(biggest_sum)
    




#import sys
#from itertools import combinations
#
#input = lambda : sys.stdin.readline().rstrip()
#
#n, m = map(int,input().split())
#c = list(map(int,input().split()))
#print(max(list(filter(lambda x : x<=m,map(sum,combinations(c,3))))))