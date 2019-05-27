n=int(input())
hexa='0123456789ABCDEF'
list=list(hexa)
rem=0
st=''
if n>15:
    while n>15:
        rem=int(n%16)
        if rem<16:
            st+=''+list[rem]
           
        n=n/16
        if n<16:
            st+=''+list[int(n)]
            break
else:
    st=''+list[int(n)]

st=st[::-1]
print(st)                

