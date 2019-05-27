import math
s=input()
s=s.replace(" ","")
row=int(math.sqrt(len(s)))
col=row+1
t=0
lt=[]
for i in range(row):
    t1=t
    t+=col
    sub=s[t1:t]
    lt.append(sub)

if t>len(s):
    t=t-col
    lt.append(s[t1:t])
else:
    lt.append(s[t:len(s)])

st=''
for j in range(col):
    for i in range(len(lt)):
        if j<len(lt[i]):
            st+=lt[i][j]
    st+=' '


print(st)    

