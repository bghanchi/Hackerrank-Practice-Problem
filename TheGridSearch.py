t=int(input())
for l in range(t):
    arr=[]
    arr1=[]
    count=0
    R,C=map(int,input().split())
    arr.clear()
    for i in range(R):
        arr.append(input())

    r,c=map(int,input().split())
    arr1.clear()
    for i in range(r):
        arr1.append(input())
          
    
    
    k=0
    arr2=[]
    i=0
    while i<len(arr):
        if k<len(arr1) and arr1[k] in arr[i]:
            k=k+1
            arr2.append(1)
        elif k==len(arr1):
            break
        else:        
            arr2.append(0)
        i=i+1

    for i in range(len(arr2)):
        if arr2[i]==1:
            j=i
            count=0
            while j<len(arr2) and arr2[j]:
                count=count+1
                j=j+1
            if count==r:
                print('YES')
                break
            else:
                print('NO')
                break            
    
             
'''
for(G_i = 0; G_i < R; G_i++){ max_index = G[0].length - P[0].length; for(k = 0; k <= max_index; k++){ match = 0; index = G[G_i].indexOf(P[0], k); if(index === -1 || G_i + r > R) continue ; 
match++; 
for(P_i=1; P_i index2 = G[G_i + P_i].indexOf(P[P_i], k); if(index2 !== index) break; match++; 
} if(match === r) break; } if(match === r) break; } if(match === r) console.log("YES"); else console.log("NO");
'''


'''
    for i in arr:
        print(i)
        if k<len(arr1) and arr1[k] in i:
                print(i)
                count=count+1
                k=k+1

    if count==r:
        print('Yes')
    else:
        print('NO')    
'''
    
