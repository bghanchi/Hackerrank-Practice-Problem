n=int(input())
scores=list(map(int,input().split()))
alice=int(input())
rank=list(map(int,input().split()))
scores=sorted(set(scores))
scores.reverse()
for i in rank:
    scores.append(i)
    scores.sort()
    scores.reverse()
    print(scores.index(i)+1)
    scores.remove(i)



'''
for i in range(alice):
    for j in range(len(scores)):
        if rank[i]<=scores[0] and rank[i]>=scores[len(scores)-1]:
            if rank[i]>=scores[j]:
                print(j+1)
                break
        elif rank[i]>scores[0]:
            print(1)
            break
        elif rank[i]<scores[0]:
            print(len(scores)+1) 
            break
'''
