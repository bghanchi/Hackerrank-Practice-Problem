m=int(input())
a = input()    
lis = a.split()
newlis = list(map(int, lis))
a1=set(newlis)
n=int(input())
b = input()
lis = b.split()
newlis = list(map(int, lis))
b1=set(newlis)

c=set(a1.intersection(b1))
d=set(a1.union(b1))

e=set(d.difference(c))
e=sorted(e)
for i in e:
    print(i)
