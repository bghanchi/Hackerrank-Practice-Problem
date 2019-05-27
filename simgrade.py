n=int(input())
a=[]
j=0
for i in range(n):
    t=int(input())
    a.append(t)  
for i in range(n):
     if (a[i]%5>2 and a[i]>=38):
         a[i]=a[i]+(5-a[i]%5)

for i in a:
    print(i)         


