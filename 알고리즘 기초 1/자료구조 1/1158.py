#q=[]
#res=[]
#N,K = map(int, input().split())
#for i in range(1,N+1):
#    q.append(i)
#        
#cnt = 1
#while len(q):
#    if cnt+K <= len(q):        
#        cnt += K-1
#    else:
#        if (len(q)-cnt < 0 and len(q) >= K) or len(q) == K:
#            cnt = K             
#        else:
#            cnt = (len(q)-cnt) + K-1
#
#    if len(q)==1:
#        res.append(q[0])           
#        q.remove(q[0])
#    else:
#        res.append(q[cnt-1])    
#        q.remove(q[cnt-1])        
#
#
#print('<',*res,'>',sep=', ')

    