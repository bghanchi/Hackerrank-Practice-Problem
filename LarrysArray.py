t=int(input())
for l in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    f=0
    for i in range(len(a)):
        if i>0 and i<=len(a)/2:
            if a[i]<a[i-1]:
                f=f+1
                break
    if f==0:
        print('NO')
    else:
        print('YES')                


'''
for l in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=''.join(map(str,a))
    c=''.join(sorted(b))
    print(b,c)
    if b==c:
        print('NO')
    else:
        print('YES')    
'''    