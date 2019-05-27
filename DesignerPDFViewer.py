s='abcdefghijklmnopqrstuvwxyz'
s=list(s)
height=list(map(int,input().split()))
st=input()
st=list(st)
arr=[]
for i in zip(*[iter(s)],*[iter(height)]):
    if i[0] in st:
        arr.append(i[1])

print(len(st)*1*max(arr))
