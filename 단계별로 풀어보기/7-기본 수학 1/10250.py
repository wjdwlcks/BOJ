
for i in range(int(input())):
    H,W,N = map(int, input().split())
    cnt=1
    while N-H>0:
        N=N-H
        cnt+=1
    print(f"{N}{format(cnt,'02')}")
    

#T = int(input())
#
#for i in range(T):
#    h, w, n = map(int, input().split( )) # h=각 호텔의 층 수, w=각 층의 방 수, n=몇 
#
#    floor = n % h 
#    room_line = (n // h) + 1
#    if floor == 0:
#        floor = h
#        room_line -= 1
#    
#    print(floor * 100 + room_line)
