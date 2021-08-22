# lambda 활용... 알아보기

N = int(input())
turn = [] 
for i in range(N): 
    data = input().split() 
    turn.append((data[0],int(data[1]),int(data[2]),int(data[3]))) 
    
turn.sort(key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0])) 

for x in turn: 
    print(x[0])

