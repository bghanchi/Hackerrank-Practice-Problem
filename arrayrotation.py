n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
b=[]
k=int(k%n)
for i in range(k):
    t=arr.pop()
    arr.reverse()
    arr.append(t)
    arr.reverse()

for i in range(q):
    index=int(input())
    print(arr[index])

