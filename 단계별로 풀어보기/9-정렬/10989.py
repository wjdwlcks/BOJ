import sys
input = sys.stdin.readline
num = int(input())
arr = [0] * 10001

for i in range(num):
    a= int(input())
    arr[a-1] += 1

for i in range(10000):
    if[arr] !=0:
        for j in range(arr[i]):
            print(i+1)


#import sys
#input = sys.stdin.readline
#num = int(input())
#arr = [0]*10000
#
#for i in range(num):
#    a = int(input())
#    arr[a-1] += 1
#    
#for i in range(10000):
#    if arr[i] != 0:
#        for j in range(arr[i]):
#            print(i+1)
#        
# # 정렬을 수행할 배열
# import sys
# arr=list()
# for i in range(int(input())):
#     arr[i]=int(input())


# count = [0] * (max(arr) + 1)


# for num in arr:
#     count[num] += 1

# for i in range(1, len(count)):
#     count[i] += count[i-1]


# result = [0] * (len(arr))


# for num in arr:

#     idx = count[num]        
#     result[idx - 1] = num
#     count[num] -= 1

# for i in result:
#     sys.stdout.write(str(i))
#     sys.stdout.write('\n')


# [1, 2, 3, 3, 4, 4, 5, 7, 9]