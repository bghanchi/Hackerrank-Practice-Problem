n=int(input())
bird=list(map(int,input().split()))
birds=set(bird)
birds=sorted(birds)
a=[]

for i in birds:
    a.append(bird.count(i))

print(birds)
print(a)
print(birds[a.index(max(a))])
'''
input()
count = [0]*6
a=map(int,input().strip().split())
for t in a:
    count[t] += 1
    print(count )
    
print(count)
print(count.index(max(count)))
'''



'''
n=int(input())
bird=list(map(int,input().split()))
birds=set(bird)
birds=sorted(birds)
a=[]
max=0
id=0
t=0
for i in birds:
    t=bird.count(i)
    if t>max:
        max=t
        id=i

print(id)        
'''

