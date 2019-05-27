n=int(input())
if n & 1:
    print('Weird')
else:
    for i in range(2,6):
        if(i==n):
            print('Not Weird')
    for i in range(6,21):
         if(i==n):
             print('Weird')       
    if(n>20):
         print('Not Weird') 