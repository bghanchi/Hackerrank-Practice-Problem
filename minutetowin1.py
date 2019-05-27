n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    if i!=0 :
        if a[i]-a[i-1]!=k:
            count=count+1
            a[i]=a[i-1]+k
    
print(count)