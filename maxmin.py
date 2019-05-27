a=input()
list=list(map(int,a.split()))
count=0
sun=0
array=[]
k=1
for i in range(5):
    sum=0
    for j in range(5):
        if(j!=count):
            sum+=list[j]

    array.append(sum)
    count=count+1

array=sorted(array)
print(array[0],'',array[4])
