x,y,w,h = map(int,input().split())
res=[]
res.append(x)
res.append(y)
res.append(w-x)
res.append(h-y)
print(min(res))

#x, y, w, h = map(int, input().split())
#print(min(x, y, w-x, h-y))