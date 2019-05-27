money,n,m=map(int,input().split())
item=list(map(int,input().split()))
buy=list(map(int,input().split()))
item.sort()
buy.sort()
sum=0
if buy[len(buy)-1]<item[len(item)-1]:
    f=0
    if item[len(item)-1]<money:
        max=item[len(item)-1]
        f=f+1                 
    else:
        i=n-1
        while i:
            if item[i]<money:
                max=item[i]
                f=f+1
                break
            i=i-1
    if f!=0: 
        for i in range(len(buy)):
            sum=max+buy[i]
            if sum>money:
                sum=max+buy[i-1]
                break
    else:
        sum=0



else:
    f=0
    if buy[len(buy)-1]<money:
        max=buy[len(buy)-1]
        f=f+1                 
    else:
        i=n-1
        while i:
            if buy[i]<money:
                max=buy[i]
                f=f+1
                break
            i=i-1    
    if f!=0:        
        for i in range(len(item)):
            sum=max+item[i]
            if sum>money:
                sum=max+item[i-1]
                break
    else:
        sum=0       

if sum==0:
    print(-1)
else:
    print(sum)    

          


