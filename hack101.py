n=int(input())
arr=list(map(int,input().split()))
s=0
po=0
a=[]
a=zip(arr, sorted(arr))
c = sum(x != y for x, y in a)
if c == 0:
    print('0')
elif c==2:
    print('1')
else:
    print('-1')
     
'''
for i in range(n):
    if i>0 and i<n:
        if arr[i]<arr[i-1]:
            s=s+1
            po=po+1

if s==0:
    print('0')
else:
    if po==2:
        print('1')
    else:
        print('-1')                    
'''
