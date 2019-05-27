n=int(input())

k=n
while k:
    for i in range(n+1):
        if i>=k:
            print('#',end='', flush=True)            
        else:
            print(end=' ')
    print(' ') 
    k=k-1            



