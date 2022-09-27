a= set()
b=set(range(1,10001))
for i in range(1,10001):    
    sum=0
    N=i
    while N :        
        if(N/10 != 0):
            sum+= N%10
            N= N//10                                   
    sum+=i
    a.add(sum)   

ret = sorted(b-a)     

for i in ret:
    print(i)


#natural_num = set(range(1, 10001))
#generated_num = set()
#
#for i in range(1, 10001):       # i = 850       
#    for j in str(i):            # j = "8", "5", "0"
#        i += int(j)             # 850 + 8 + 5 + 0, i = 863
#    generated_num.add(i)        # 생성자가 있는 숫자들
#
#self_num = sorted(natural_num - generated_num)
#for i in self_num:
#    print(i)



## 함수 d(n)
#def d(n):
#    # 생성자 n을 이용해 d(n)을 만드는 수식
#    n = n + sum( map(int, str(n)) )
#    return n
#
## 셀프 넘버가 아닌 수들(생성자가 있는 수들)이 들어갈 집합
#nonSelfNum = set()
#
## nonSelfNum 집합에 들어갈 수들을 찾아 넣기
#for i in range(1, 10001):
#    nonSelfNum.add( d(i) )
#
## 셀프 넘버들을 출력하기
#for j in range(1, 10001):
#    if j not in nonSelfNum:
#        print(j)




#numbers = list(range(1, 10_001))
#remove_list = []  # 이후에 삭제할 숫자 list
#for num in numbers :
#    for n in str(num):
#        num += int(n)  # 생성자가 있는 숫자
#    if num <= 10_000:  # 10,000보다 작거나 같을 때만,
#        remove_list.append(num)  # append: 리스트에 요소를 추가할 때
#
#for remove_num in set(remove_list) :  # set 으로 중복값 제거
#    numbers.remove(remove_num)
#for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
#    print(self_num)


        
        