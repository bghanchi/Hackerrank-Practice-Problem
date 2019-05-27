n,k=map(int,input().split())
arr=list(map(int,input().split()))
i1=0
count=0
for i in range(n):
    j=i+1
    f=0
    while j<n:
        if sum(arr[i:j])%k!=0:
            f=f+1
            break
        j=j+1       
    if f!=0:
        i1=i
        break    

j=i1+1
while j<n:
    if (arr[i1]+arr[j])%k!=0:
        count=count+1
    j=j+1   

print(count*2-1)
