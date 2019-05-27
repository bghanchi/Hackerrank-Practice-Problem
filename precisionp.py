n=int(input())
a=[]
list=list(map(int,input().split()))
pos=0
neg=0
zero=0
for i in list:
    if i>0:
        pos=pos+1
    elif i<0:
        neg=neg+1
    else:
        zero=zero+1


print(format(pos/n,'.6f'))                
print(format(neg/n,'.6f'))                
print(format(zero/n,'.6f'))                