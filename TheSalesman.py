q=int(input())
for i in range(q):
    n=int(input())
    house=list(map(int,input().split()))
    house.sort()
    print(house[n-1]-house[0])