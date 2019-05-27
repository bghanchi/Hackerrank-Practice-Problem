'''
s = input()
a=s.split()
list1=list(a)
list3=[]
for i in list1:
    i=i.capitalize()
    list3.append(i)

j=0
for i in s.split():
    s=s.replace(i,list3[j])
    j=j+1

print(s)    
''' 
    


'''
result=solve(s)
print(result)
'''



'''
for x in s[:].split():
    s = s.replace(x, x.capitalize())
    print(s)
print(s)
'''





'''s=input().split()
list1=list(s)
list3=[]
j=0
for i in list1:
    list2=list(i)
    list2[0]=i[0].upper()
    list3.append(list2)

str=''
for i in list3:
    str+=''.join(i)+' '

print(str)    

'''