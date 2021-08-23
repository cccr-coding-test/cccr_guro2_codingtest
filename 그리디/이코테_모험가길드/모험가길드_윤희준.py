n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 
c = 0  

for i in data: 
    c += 1 
    if c >= i: 
        result += 1 
        c = 0 

print(result)