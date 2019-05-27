'''
s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
print((n // len(s)))
'''

s=input()
s.lower()
n=int(input())
x=s.count('a')
y=n//len(s)
print(y)
rem=n%len(s)
sub=s[0:rem]
print(sub)
z=sub.count('a')
print(z)
result=y*x+z
print(int(result))


'''
if n>10000:
    x=s.count('a')
    y=round(x*(n/len(s)))
    print(y)


else:    
    while t<=n:
        s=s+s1
        t=t+t1

    t2=n-(t-t1)
    sub=s1[0:t2]
    s=s+sub
    print(s.count('a')-s1.count('a'))    
'''
