from collections import Counter
import sys
input = sys.stdin.readline
a=list()
mode=0
N = int(input())
for i in range(N):
    a.append(int(input()))

a.sort()
mode=Counter(a).most_common()

print(round(sum(a)/N))
print(a[N//2])
if len(a) > 1 :
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])    
else :
    print(mode[0][0])        

print(max(a)-min(a))





#n = int(input())
#
#nums = []
#for _ in range(n) :
#	nums.append(int(input()))
#
## 산술평균
#print(round(sum(nums)/n))
#
## 중앙값
#nums.sort()
#print(nums[int((n-1)/2)])
##
### 최빈값
#counts = dict()
#for i in range(1,n+1) :
#	counts[i] = []
#
#maxCount = 1
#count = 1
#for j in range(1,n) :
#	if nums[j] == nums[j-1] :
#		count += 1
#	else :
#		counts[count].append(nums[j-1])
#		if maxCount < count : maxCount = count
#		count = 1
#	if j == n-1 : 
#		counts[count].append(nums[j])
#		if maxCount < count : maxCount = count
#
#if n == 1 :
#	counts[1].append(nums[0])
#
#counts[maxCount].sort()
#if len(counts[maxCount]) == 1 :
#	print(counts[maxCount][0])
#else :
#	print(counts[maxCount][1])
#
## 범위
#print(nums[-1]-nums[0])