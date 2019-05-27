n,k=map(int,input().split())
R,C=map(int,input().split())
ob=[]
count=0
for i in range(k):
    k,j=map(int,input().split())
    ob.append([k,j])

### UP
f=0
for r in ob:
    if R<r[0] and C==r[1]:
        count+=r[0]-R-1
        f=f+1
        break
if f==0:
    count+=n-R        

### down
f=0
for r in ob:
    if R>r[0] and C==r[1]:
        count+=R-r[0]-1
        f=f+1
        break

if f==0:
    count+=R-1        

###left
f=0
for r in ob:
    if R==r[0] and r[1]<C:
        count+=C-r[1]-1
        f=f+1
        break
        
if f==0:
    count+=C-1        

### right
f=0
for r in ob:
    if R==r[0] and C<r[1]:
        count+=r[1]-C-1
        f=f+1
        break

if f==0:
    count+=n-C        

###upright
f=0
for r in ob:
    if R<r[0] and C<r[1] and (r[0]-R)==(r[1]-C):
        count+=r[0]-R-1
        f=f+1
        break

if f==0:
    count+=n-R        

###downleft
f=0
for r in ob:
    if R>r[0] and C>r[1] and (R-r[0])==(C-r[1]):
        count+=R-r[0]-1
        f=f+1
        break

if f==0:
    if R>C:
        count+=C-1
    else:
        count+=R-1            


###downright
f=0
for r in ob:
    if R>r[0] and C<r[1] and (R-r[0])==(r[1]-C):
        count+=r[1]-C-1
        f=f+1
        break
if f==0:
    count+=n-C

###upleft
f=0
for r in ob:
    if R<r[0] and C>r[1] and (r[0]-R)==(C-r[1]):
        count+=r[0]-R-1
        f=f+1
        break
if f==0:
    count+=n-R
print(count)


'''
for i in range(k):
    k,j=map(int,input().split())
    ob.append([k,j])

for r in ob:
    if r[0]<R and r[1]==C:
        count+=R-r[0]-1
        print(count)
    else:
        count+=R-1
        print(count)

    if R<r[0] and r[1]==C:
        count+=r[0]-R-1
        print(count)

    else:
        count==n-R 
        print(count)

   
    if r[1]<C and r[0]==R:
        count+=C-r[1]-1
        print(count)

    else:
        count+=C-1
        print(count)

    if C<r[1] and r[0]==R:
        count+=r[1]-C-1
        print(count)

    else:
        count+=n-C
        print(count)
     
    
    if r[0]<R and r[1]<C:
          if (R-r[0])==(C-r[1]):
              count+=R-r[0]-1
              print(count)

          else:
              count+=C-0
              print(count)

    elif R<r[0] and C<r[1]:
        if(r[0]-R)==(r[1]-C):
            count+=r[0]-R-1
            print(count)

        else:
            count+=n-R
            print(count)

                          
    if r[0]<R and C<r[1]:
          if (R-r[0])==(r[1]-C):
              count+=R-r[0]-1
              print(count)

          else:
              count+=n-C
              print(count)

    elif R<r[0] and r[1]<C:
          if (r[0]-R)==(C-r[1]):
              count+=r[0]-R-1
              print(count)

          else:
              count+=n-R
              print(count)


print(count)

'''
