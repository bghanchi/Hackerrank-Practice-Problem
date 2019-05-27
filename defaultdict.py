from collections import defaultdict
d = defaultdict(list)
a, b = map(int,input().split())
l1=[]
for i in range(a):
    d[input()].append(i+1) 

for i in range(b):
    l1.append(input())

for i in l1:
    if i in d:
        print(" ".join( map(str,d[i])))
    else:
        print(-1)


             


###if 'bharat'in d:
###    print('hai bharat kumar')

'''
for i in range(0,m):
    list1=list1+[input()]  

for i in list1: 
    if i in d:
        print(" ".join( map(str,d[i])))
    else:
        print(-1)
'''

'''
from collections import defaultdict
d = defaultdict(list)
a,b=map(int,input().split())
for i in range(a):
    d['A'].append(input())
for i in range(b):
    d['B'].append(input())

l1=[]
l2=[]
l1=d.get('B')
l2=d.get('A')
f=0
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            f=f+1
            print(j+1,end=' ', flush=True)

    if f==0:
        print(-1)
    print(' ')    
'''