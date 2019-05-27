t=int(input())
for i in range(t):
    n,m,s=map(int,input().split())
    s=s-1+m
    if s>n:
        print(s-n)
    else:
        print(s)    
    

