s=input()



def solve(s):
    a,b=s.split()
    list1=list(a)
    list2=list(b)
    list1[0]=a[0].upper()
    list2[0]=b[0].upper()
    a=''.join(list1)
    b=''.join(list2)
    return (a+' '+b)



result=solve(s)
print(result)