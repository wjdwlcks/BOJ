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
        print(1 , end=' ')
    else:
        print(0 , end=' ')


# import sys

# n = int(input())
# card = list(map(int, sys.stdin.readline().split()))
# m = int(input())
# check = list(map(int, sys.stdin.readline().split()))

# card.sort()

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2

#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None


# for i in range(m):
#     if binary_search(card, check[i], 0, n - 1) is not None:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
