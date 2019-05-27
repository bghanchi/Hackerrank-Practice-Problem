st=input()
st=list(st)
f=0
for i in st:
    if i.isalnum():
        print('True')
        f=f+1
        break
if f==0:
    print('False')                

f=0
for i in st:
    if i.isalpha():
        print('True')
        f=f+1
        break
if f==0:
    print('False')                

f=0
for i in st:
    if i.isdigit():
        print('True')
        f=f+1
        break
if f==0:
    print('False')

f=0
for i in st:
    if i.islower():
        print('True')
        f=f+1
        break
if f==0:
    print('False')                

f=0
for i in st:
    if i.isupper():
        print('True')
        f=f+1
        break
if f==0:
    print('False')                





'''
print(st.isalnum())
print(st.isalpha())
print(st.isdigit())
print(st.islower())
print(st.isupper())
'''