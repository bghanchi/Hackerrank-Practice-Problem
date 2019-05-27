s=input()
str=list(s)
index,ch=input().split()
index=int(index)
str[index]=ch
s=''.join(str)
print(s)
