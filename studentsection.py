n1=int(input())
a=[]
sum=0
for j in range(n1): 
    n,k,m=map(int,input().split())
    a=list(map(int,input().split()))  
    for i in range(m):
        sum=sum+a[i]
        if sum>=k:
            print(i+1)
            break

