str=input()
str=str.upper()
strr=str
str=list(str)
a=set()
str1=''
st=0
ke=0
for i in range(len(str)):
    t=i
    for j in range(len(str)):
        l=j
        k=t+j
        while(l<=k and k<len(str)):
            str1+=str[l]
            l=l+1
        a.add(str1)
        str1=''    

a=sorted(a)
a.pop(0)
for i in a:
    string=list(i)
    ch=string.pop(0)
    if (ch!='A'and ch!='E'and ch!='I' and ch!='O' and ch!='U'):
        st+=strr.count(i)
    else:
        ke+=strr.count(i)


print(st)
print(ke)