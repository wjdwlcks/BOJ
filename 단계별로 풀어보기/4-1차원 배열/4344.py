for i in range(int(input())):
    cnt=0
    a= list(map(int, input().split()))
    avg = sum(a[1:])/a[0]
    for j in a[1:]:
            if j>avg:
                cnt+=1
    print(f"{cnt/a[0]*100:.3f}%")

        
num = int(input())

#for _ in range(num):
#    scores = list(map(int, input().split()))
#    avg = sum(scores[1:])/scores[0]
#    
#    cnt = 0
#    for i in scores[1:]:
#        if i > avg:
#            cnt += 1
#            
#    per = (cnt/scores[0])*100
#    print('%.3f' %per + '%')