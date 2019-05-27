st=input()
n=int(input())
st1=''
j=0
for i in range(len(st)):
    st1+=''+st[i]
    j=j+1    
    if j==n or i==len(st)-1:
        print(st1)
        st1=''
        j=0
    