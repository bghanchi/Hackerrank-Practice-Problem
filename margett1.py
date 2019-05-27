s= input() 
s1=input()
for part in zip(*[iter(s)],*[iter(s1)]):
    print(part)


'''
s= input() 
n=int(input())
for part in zip(*[iter(s)] * n):
    b=sorted(set(part),key=part.index)
    print(''.join(b))
'''
###    d = dict()
###    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))