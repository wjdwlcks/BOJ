a=[0 for i in range(26)]
cnt = 0

for i in input():
    index= int(ord(i.lower())-97)    
    a[index]+= 1

max = max(map(int,(a)))

for i in range(len(a)):
    if(a[i]==max):        
        asc= i + 65
        alphabet=chr(asc)
        cnt+=1
if(cnt>1):
    print('?')
else:
    print(alphabet)


#    words = input().upper()
#unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거
#
#cnt_list = []
#for x in unique_words :
#    cnt = words.count(x)
#    cnt_list.append(cnt)  # count 숫자를 리스트에 append
#
#if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
#    print('?')
#else :
#    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
#    print(unique_words[max_index])


 
    
