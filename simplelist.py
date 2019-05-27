n=int(input())
a=[]
while n:
    c=input().split()
    if c[0]=='insert':
        a.insert(int(c[1]),int(c[2]))
          
    elif c[0]=='append':
        a.append(int(c[1]))

    elif c[0]=='remove':
        a.remove(int(c[1]))

    elif c[0]=='print':
        print(a)

    elif c[0]=='reverse':
        a.reverse()

    elif c[0]=='sort':
        a=sorted(a)

    elif c[0]=='pop':
        a.pop()

    n=n-1