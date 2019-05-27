n=input()
a=input()
a=a.upper()
s=list(a)
level=0
count=0

for i in range(len(s)):
    if level==0 and s[i]=='D':
            count=count+1

    if s[i]=='U':
        level=level+1
    else:
        level=level-1
    


print(count)
