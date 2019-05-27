import math
t=int(input())
for j1 in range(t):
    count=0
    a,b=map(int,input().split())
    i=a
    while i>=a and i<=b:
            j=2
            while j<=int(i/2):
                if j*j==i:
                    count=count+1
                j=j+1
            i=i+1
    print(count)         


'''
for j1 in range(t):
    count=0
    a,b=map(int,input().split())
    a1=int(math.sqrt(a))
    b1=int(math.sqrt(b))
    if a1!=b1:
        if a1<=1:
            a1=a1+1
            while a1<=b1 and a1>1:
                count=count+1
                a1=a1+1
            print(count)
        else:
            while a1<=b1 and a1>1:
                count=count+1
                a1=a1+1
            print(count)


    else:
        print(0)
'''

'''
for j1 in range(t+1):
    count=0
    a,b=map(int,input().split())
    i=a
    while i>=a and i<=b:
            j=2
            while j<=int(i/2):
                if j*j==i:
                    count=count+1
                j=j+1
            i=i+1
    print(count)         
'''
'''
def square(a):
    j=2
    f=0
    while j<=int(a/2):
        if j*j==a:
            f=f+1
            break
        j=j+1    
    if f==0:
        return 1
    else:
        return 0            
'''