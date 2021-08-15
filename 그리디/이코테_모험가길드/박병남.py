n=int(input())
scarys=list(map(int,input().split()))
scarys.sort(reverse=True)
result,people,max_scary=0,0,1

while scarys:
    scary=scarys.pop()
    people+=1
    max_scary=max(scary,max_scary)
    if max_scary==people:
        result+=1
        people=0

print(result)
