n=int(input())
str1=''
rem=0
st=''
if n>1:
    while n>1:
        rem=int(n%2)
        st+=''+str(rem)
        n=n/2
        if n==1:
            st+=''+str(int(n))
            break; 
else:
    st+=''+str(int(n))

st=st[::-1]
print(st)
