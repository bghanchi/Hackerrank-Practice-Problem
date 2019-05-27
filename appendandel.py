s=input()
s1=input()
s.lower()
s1.lower()
k=int(input())
i=len(s1)
j=0
while i>0:
    s2=s1[0:i]
    if s.count(s2):
        break
    j=j+1
    i=i-1

total=len(s)-len(s2)
total=total+j


if k>=total:
    if k>=len(s)+len(s1):
        print("Yes"); 
    else: 
        if (k-total)%2==0: 
            print("Yes")
        else:
            print("No")
    

else: 
    print("No"); 
 
'''
if s==s1:
    print('Yes')
else:    
    while i>0:
        s2=s1[0:i]
        if s.count(s2):
            break
        j=j+1
        i=i-1

    total=len(s)-len(s2)
    total=total+j
    if total==k:
        print('Yes')
    else:
        print('No')    
'''