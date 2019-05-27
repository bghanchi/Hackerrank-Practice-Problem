a1,b1=input().split()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=sorted(a)
b=sorted(b)
i=a[len(a)-1]
count=0
if i<=b[0]:
    while i<=b[0]:
        f=0
        k=0
        for j in a:
            if i%j!=0:
                f=f+1
        if f==0:
            for b1 in b:
                if b1%i!=0:
                    k=k+1
                    break
        if k==0 and f==0:
            count=count+1            
             
        i=i+1
else:
    print(count)


print(count)                        