a=input()
a=a.upper()
ke = 0
st = 0
i=0
while i<len(a):
    if(a[i]!='A'and a[i]!='E'and a[i]!='I' and a[i]!='O' and a[i]!='U'):
        st+= (len(a)-i)
    else:
        ke+= (len(a)-i)
    i=i+1

if ke!=st:
    if ke>st:
        print("Kevin", ke)
    else:
        print("Stuart",st)
else:
    print("Draw")