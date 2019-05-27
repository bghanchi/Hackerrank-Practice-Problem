import string
n=int(input())
a=[]
b=[]
c=[]
for i in range(n):
    name=input()
    marks=float(input())
    b.append(name)
    b.append(marks)
    a.append(b)
    b=[]
 

sorted(a,reverse=True)
for i in range(n):
    j=i+1
    for j in range(n):
        if a[i][1]>a[j][1]:
            t=a[j]
            a[j]=a[i]
            a[i]=t

i=len(a)-1
secondmin=0
while(i>=0):
    j=i-1
    while(j>=0):
        if(a[j][1]>a[i][1]):
            secondmin=a[j][1]
            break
        j=j-1

    i=i-1     
    break

for i in range(n):
    if a[i][1]==secondmin:
        c.append(a[i][0]) 

c.sort()
for i in range(len(c)):
      print(c[i])
