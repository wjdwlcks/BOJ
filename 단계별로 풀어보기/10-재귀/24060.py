import sys
import math

def merge_sort(arr,res):
    def sort(low,high):
        if high-low < 2:
            return
        mid = math.ceil((high+low)/2)
        sort(low,mid)
        sort(mid,high)
        merge(low,high,mid)
    def merge(low,high,mid):

        temp=[]       
        l,h=low,mid
        while l<mid and h<high:
            if arr[l] < arr[h]:
                temp.append(arr[l])                
                #res.append(arr[l])                
                l+=1
            else:
                temp.append(arr[h])
                #res.append(arr[h])                
                h+=1
        while l<mid:
            temp.append(arr[l])
            #res.append(arr[l])                
            l+=1    
        while h<high:
            temp.append(arr[h])
            #res.append(arr[h])                
            h+=1   
        for i in range(low,high):            
            arr[i] = temp[i-low]
            res.append(temp[i-low])            
    return sort(0,len(arr))


a=list()
res=list()
N,K = map(int,input().split())
a=list(map(int,sys.stdin.readline().split()))

merge_sort(a,res)
if len(res)<K:
    print(-1)
else:    
    print(res[K-1])    