from collections import defaultdict

M=int(input())
list1= sorted(list(map(int,input().split())))
M=int(input())
cards= list(map(int,input().split()))

cnt=defaultdict(int)

for i in list1:
    cnt[i]+=1


for i in cards:
    if int(i) in cnt:
        print(cnt[i] , end=' ')
    else:
        print(0 , end=' ')


# def bs(l, target, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if l[mid] == target:
#         return cnt.get(target)
#     elif l[mid] > target:
#         return bs(l, target, start, mid-1)
#     else:
#         return bs(l, target, mid+1, end)

# n = int(input())
# a = sorted(list(map(int, input().split())))
# m = int(input())
# b = list(map(int, input().split()))

# cnt = {}
# for i in a:
#     if i in cnt:
#         cnt[i] += 1
#     else:
#         cnt[i] = 1

# for i in b:
#     print(bs(a, i, 0, len(a)-1), end=' ')        