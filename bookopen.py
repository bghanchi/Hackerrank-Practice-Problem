n=int(input())
p=int(input())
front=0
back=0
front=int(p/2)
back=int((n-p)/2)
print(min(front,back))
'''
if front<back:
    print(front)
else:
    print(back)    
'''    