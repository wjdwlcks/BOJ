import sys

def merge_sort(arr):
    def sort(low,high):
        if high - low <2:
            return 
        mid = (low+high)//2
        sort(low,mid)
        sort(mid,high)
        merge(low,mid,high)
        return arr

    def merge(low,mid,high):
        temp = []
        l,h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l+=1
            else :
                temp.append(arr[h])
                h+=1
        while l < mid:
            temp.append(arr[l])
            l+=1
        while h < high:
            temp.append(arr[h])
            h+=1
        
        for i in range(low,high):
            arr[i] = temp[i-low]

    return sort(0,len(arr))                

a= list()
for i in range(int(input())):
    a.append(int(sys.stdin.readline()))

merge_sort(a)
for i in a:
    sys.stdout.write(str(i))
    sys.stdout.write('\n')
    




# def merge_sort(arr):
#     if len(arr)<2:
#         return arr
    
#     mid = len(arr)//2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])


#     merged_arr = []
#     l=h=0

#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l+=1
#         else:
#             merged_arr.append(high_arr[h])
#             h+=1
#     merged_arr+= low_arr[l:]            
#     merged_arr+= high_arr[h:]
#     print('low:',low_arr)
#     print('high:',high_arr)
#     print('merge:',merged_arr)    
#     return merged_arr


#import sys
#n = int(input())
#l = []
#for i in range(n):
#    l.append(int(sys.stdin.readline()))
#for i in sorted(l):
#    sys.stdout.write(str(i)+'\n')
