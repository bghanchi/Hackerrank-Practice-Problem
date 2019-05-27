n=int(input())
arr=list(map(int,input().split()))
b=set(arr)
b=sorted(b)
max=[]
sum=0
for i in b:
    sum+=arr.count(i)
    sum+=arr.count(i+1)
    max.append(sum)
    sum=0

max.sort()
print(max[len(max)-1])


