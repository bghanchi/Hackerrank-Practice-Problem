n1=int(input())
w=len(bin(n1)[2:])
print(w)
def binaray(n):
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
    return st


def octal(n):  
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
    return st


def hexa(n):
    hexa='0123456789ABCDEF'
    list1=list(hexa)
    rem=0
    st=''
    if n>15:
        while n>15:
            rem=int(n%16)
            if rem<16:
                st+=''+list1[rem]
            
            n=n/16
            if n<16:
                st+=''+list1[int(n)]
                break
    else:
        st=''+list1[int(n)]

    st=st[::-1]
    return st


for i in range(n1+1):
    if i>0:
        print(str(i).rjust(w,' '),octal(i).rjust(w,' '),end=' ')
        print(hexa(i).rjust(w,' '),binaray(i).rjust(w,' '),sep=' ')       
 


    
  
       
  