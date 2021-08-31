n=int(input())
houses=list(map(int,input().split()))
houses.sort()
print(houses[n//2-1])
