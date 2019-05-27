q=int(input())
for i in range(q):
    n=int(input())
    M=[]
    count=0
    for i in range(n):
        M.append(list(map(int, input().rstrip().split())))
    for i in range(n):
        index=M[i].index(max(M[i]))
        sum=0
        sum1=0
        for j in range(n):
            if j!=index:
                sum+=M[i][j]
            if i!=j:
                sum1+=M[j][index]
        if sum==sum1:
            count=count+1
    if count!=0:
        print('Possible')
    else:
        print('Impossible')            

    
