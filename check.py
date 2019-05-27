n = int(input())
j=len("{0:b}".format(n))
print(j)
for i in range(1,n+1):
    print("{0:{j}d},{0:{j}o},{0:{j}X},{0:{j}b}".format(i,j=j))


'''
s=input()
print(s.split(' '))
str=' '
for i in s.split(' '):
  print(i.capitalize())
  str+=i.capitalize()+' '

print(str)  
'''




'''
import string 
print(string.capwords(input(), ' '))
'''



'''
st=input()
subst=input()
sum=0
for i in range(len(st)-len(subst)+1):
    if st[i:i+len(subst)] == subst:
      sum+=1

print(sum)      
'''




'''
number=int(input())
w = len(format(number, 'b'))
for i in range(1, number+1):
    d = str(i)
    o = format(i, 'o')
    h = format(i, 'X')
    b = format(i, 'b')
    print(d, o, h, b)

'''

'''n = int(input())
j=len("{0:b}".format(n))
print(j)
for i in range(1,n+1):
  print("{0:{j}d},{0:{j}o},{0:{j}X},{0:{j}b}".format(i,j=j))
'''