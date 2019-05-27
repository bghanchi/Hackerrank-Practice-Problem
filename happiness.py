n,m=map(int,input().split())
arr=list(map(int,input().split()))
setlist=[]
happiness=0
for i in range(0,2):
    a=set(map(int,input().split()))
    setlist.append(a)

for i in arr:
    if i in setlist[0]:
        happiness+=1
    elif i in setlist[1]:
        happiness+=-1

print(happiness)            
