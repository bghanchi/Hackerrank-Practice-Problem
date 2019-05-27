d1,m1,y1=map(int,input().split())
d2,m2,y2=map(int,input().split())
if y1==y2:
    if m1==m2:
        if d1<d2:
            print(0)
        else:
            print(15*(d1-d2)) 
    else:
        if m1<m2:
            print(0)
        else:    
           print(500*(m1-m2))

else:
    if y1<y2:
        print(0)
    else:    
        print(10000)                   
