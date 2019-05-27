t=int(input())
for l in range(t):
    n,k=map(int,input().split())
    i=1
    pos=[]
    arr=[]
    arr.insert(0,0)
    f=0
    for i in range(1,n+1):
        pos.append(i)
    f=0
    for i in range(n):
        f=0
        for j in range(1,n+1):
            if i>j and i-j==k:
                f=f+1
                break
            elif i<=j and j-i==k:
                f=f+1
                break
        if f==0 and k!=0:
            print('-1')
            break
    if k==0:
        print(*pos)

    elif f!=0 and k!=0:
        for i in pos:
            for j in range(1,n+1):
                if i>j and i-j==k:
                    arr.insert(j,i)
                    break
                elif i<j and j-i==k:
                    t1=j-i
                    arr.insert(t1,i)
                    break
        print(*arr[1:n+1])            


'''   
    for i in range(1,n+1):
            pos.append(i)
 
    for i in range(n):
        if pos[i]>k:
            t1=pos[i]-k
            print(t1)
            if t1<n:
                arr.insert(t1,pos[i])
            else:
                f=f+1    
        elif pos[i]<=k:
            t1=pos[i]+k
            print(t1)
            if t1<n:
                 arr.insert(t1,pos[i])
            else:
                f=f+1   
    print(arr)            
'''




'''
    for i in range(n):
        if pos[i]>k:
            t1=pos[i]-k
            if t1<n:
                arr.insert(t,pos[i])
            else:
                f=f+1
        elif pos[i]<k:
            t1=pos[i]+k
            if t1<n:
                arr.insert(t,pos[i])
            else:
                f=f+1
        elif pos[i]==k:
            t1=pos[i]*2
            if t1<n:
                arr.insert(t,pos[i])
            else:
                f=f+1
    if f==0:
        print(arr)
    else:
        print('-1')            
             
'''