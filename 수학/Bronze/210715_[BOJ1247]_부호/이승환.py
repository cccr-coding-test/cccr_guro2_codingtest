import sys
 
answer = []
 
for i in range(3):
    n = int(sys.stdin.readline())
    sum = 0
    for j in range(N):
        m = int(sys.stdin.readline())
        sum += m
    
    if sum > 0:
        answer.append("+")
    elif sum < 0:
        answer.append("-")
    else:
        answer.append("0")
 
for k in answer:
    print(k)