def print_rangoli(n):
    alpha='abcdefghijklmnopqrstuvwxyz'
    a=list(alpha)
    list1=[]
    list2=[]
    for i in range(n):
        list1.append(a[i])

    list1.reverse()
    for i in range(len(list1)):
        if i==0:
            str=list1[i]
            list2.append(str)
        else:
            k=str[::-1]
            t=str+list1[i]+k
            list2.append(t)
            str=str+list1[i]
    
    list1=[]
    for i in list2:
        list1.append("-".join(i))

    i=0
    k=n*2-2 
    while i<n:
        str="-"*k+list1[i]+"-"*k
        print(str)
        k=k-2
        i=i+1
    
    k=2
    i=i-2
    while i>=0:
        str="-"*k+list1[i]+"-"*k
        k=k+2
        print(str)
        i=i-1
        






n = int(input())
print_rangoli(n)