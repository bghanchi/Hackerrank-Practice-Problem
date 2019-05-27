n=int(input())
st=''

if n>7:
    while n>7:
        rem=int(n%8)
        st+=''+str(int(rem))
        n=n/8
        if n<8:
            st+=''+str(int(n))
            break
else:
    st+=''+str(n)

st=st[::-1]
print(st)                