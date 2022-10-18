from collections  import deque

dq = deque()

for i in range(int(input()),0,-1):
    dq.append(i)

while len(dq) > 1:
    dq.pop()
    dq.appendleft(dq[-1])
    dq.pop()
#    dq.popleft()
#    move_num = dq.popleft()
#    dq.append(move_num)    

print(*dq)    

#input = int(input())
#square = 2
#
#while True:
#    if (input == 1 or input == 2):
#        print(input)
#        break
#    square *= 2
#    if (square >= input):
#        print((input - (square // 2)) * 2)
#        break




#import sys
#
#N = int(sys.stdin.readline())
#
#arr = [i+1 for i in range(N)]
#
#while len(arr) > 1:
#    if len(arr) % 2:
#        t = [arr[-1]]
#        t.extend(arr[1::2])
#        arr = t
#    else:
#        arr = arr[1::2]
#        
#
#print(arr[0])

