a=[]
for i in  range(int(input())):
    a.append(int(input()))

a.sort()

for i in a:
    print(i)


# N = int(input())
# M = set()
# for i in range(N) :
# 	M.add(int(input()) #append대신에 add사용
# M = list(M)
# M.sort()
# for i in range(len(M)) : 
# 	print(M[i])    


# 버블 정렬
# N = int(input())

# M = []

# for i in range(N) : 
#     M.append(int(input()))

# # Bubble Sort
# for i in range(len(M)) : 
#     for j in range(len(M)) : 
#         if M[i] < M[j] : 
#             M[i], M[j] = M[j], M[i]
            
# for n in M : 
#     print(n)    


# 삽입 정렬
#N = int(input())
#M = []
#
#for i in range(N) : 
#    M.append(int(input()))
#
## Insert Sort
#for i in range(1, len(M)) :
#    while (i>0) & (M[i] < M[i-1]) :
#        M[i], M[i-1] = M[i-1], M[i]
#        
#        i -= 1
#        
#for n in M : 
#    print(n)