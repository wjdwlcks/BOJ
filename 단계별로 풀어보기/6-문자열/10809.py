word = input()

# 영어 소문자는 아스키코드 97~122
alphabet = list(range(97,123))

for i in alphabet:
    print( word.find(chr(i)) )


#S = input()
#abc ='abcdefghijklmnopqrstuvwxyz'
#
#for i in abc:
#    if i in S:
#        print(S.index(i), end= ' ')
#    else:
#        print( -1, end =' ')    