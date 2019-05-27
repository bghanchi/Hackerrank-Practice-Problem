st=input().upper()
subst=input().upper()
sum=0
for i in range(len(st)):
    if st[i]==subst[0]:
        j=i
        f=0
        for k in range(len(subst)):
            if st[j]==subst[k]:
                j=j+1
                if j>=len(st):
                    i=j
                    break
            else:
                f=f+1
        if(f==0):
            sum+=1
    if i>=len(st):
        break

print(sum)

