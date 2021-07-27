n,m,k=map(int, input().split())
li=list(map(int,input().split()))

li.sort(reverse=True)
first=li[0]   # 큰수
second=li[1]  # 작은수
result=0
result=first*(m-(m//(k+1)))+second*(m//(k+1))

print(result)