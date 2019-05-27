n,a=map(int,input().split())
arr=list(map(int,input().split()))
b=[]
max=[]
count=0
for i in range(len(arr)-1):
    t=arr[i+1]-arr[i]
    b.append(t)

c=set(b)
c=list(c)
for i in c:
    max.append(b.count(i))

max=sorted(max)
d=max[len(max)-1]

for i in range(len(arr)):
    if i!=0:
      if arr[i-1]+d!=arr[i]:
          arr[i]=arr[i-1]+d
          count=count+1

print(count)
