a=list()
rank = list()
cnt=0
for i in range(int(input())):
      a.append(list(map(int,input().split())))

for i in range(len(a)): 
      cnt=1
      for j in range(len(a)):                      
            if a[i][0] <  a[j][0] and a[i][1] <  a[j][1]:
                  cnt+=1
      rank.append(cnt)

print(*rank)            


#N = int(input()) #전체 사람 수
#people = [] #사람 정보를 받을 list
#
#for _ in range(N): #입력한 순서대로 정보를 입력받는다.
#    x, y = map(int, input().split())
#    people.append((x,y))
#
#for i in people:
#    rank = 1 #초기값은 전부 1
#    for j in people:
#        if i[0] < j[0] and i[1] < j[1]: #조건
#            rank+=1 #조건 만족 시 count up
#    print(rank, end = " ") #바로 출력

                  
