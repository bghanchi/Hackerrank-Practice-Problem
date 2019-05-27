n=int(input())
arr=list(map(int,input().split()))
arr1=[]
for x in range(1,n+1):
    index=arr.index(x)
    index=index+1
    for j in range(len(arr)):
        if arr[j]==index:
            print(j+1)

