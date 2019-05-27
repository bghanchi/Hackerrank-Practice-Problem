str=input()
j=len(str)
k=''
for i in range(len(str)):
    if str[i].isupper():
        k+=str[i].lower()
    else:
        k+=str[i].upper()    

print(k)        