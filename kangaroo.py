x1,v1,x2,v2=map(int,input().split())
if x1>x2 and v1>v2:
    print('NO')
elif x2>x1 and v2>v1:
    print('NO')
else:
    f=0
    d1=x1
    d2=x2
    while 1:
        d1=d1+v1
        d2=d2+v2
        if d1==d2:
            f=f+1
            break

    if f==0:
        print('NO')
    else:
        print('YES')                    