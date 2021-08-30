N = int(input())
location = list(map(int,input().split()))
location.sort()
antenna = location[(N-1)//2]
print(antenna)