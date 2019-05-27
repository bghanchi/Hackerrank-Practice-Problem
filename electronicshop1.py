money,n,m=map(int,input().split())
item=list(map(int,input().split()))
buy=list(map(int,input().split()))
item.sort()
item.reverse()
buy.sort()
buy.reverse()
max=0
f=0
b=[]
for i in item:
    for j in buy:
        sum=i+j
        if i+j<=money:
            b.append(sum)
            f=f+1
            break
        
if f==0:
    print(-1)          
else:
    b.sort()
    print(b[len(b)-1])
      