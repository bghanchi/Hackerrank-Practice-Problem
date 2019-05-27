n=int(input())
list=[]
for i in range(n):
    k=input()
    list.append(k)

b=[]
string='0123456789'
count=0
for i in range(n):
    j=i
    while j<n:
        if list[i]!=list[j]:
            a=str(list[i])+str(list[j])
            a=set(a)
            if ' 'in a:
                a.remove(' ')
                a=sorted(a)
                a=''.join(a)
            else:
                a=sorted(a)
                a=''.join(a)
            if a==string:
                print(list[i],list[j])
                print(a)
                count=count+1    

        j=j+1


print(count)        
### print(b)        



'''
for i in list:
    for j in list:
        b.append(i+j)
        i=sorted(i)
        j=sorted(j)
        print(i,' ',j)
        c=set(i+j)
        c=list(c)
        f=0
        for k in range(0,9):
            if k not in c:
                f=f+1
                break
        if f==0:
            count=count+1        

print(count)
'''
