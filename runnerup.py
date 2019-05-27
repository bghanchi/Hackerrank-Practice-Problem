n=int(input())
a=input()
list=list(map(int,a.split()))
list=sorted(list)
i=len(list)-1
while i:
    if list[i]!=list[len(list)-1]:
        print(list[i])
        break; 

    i=i-1           