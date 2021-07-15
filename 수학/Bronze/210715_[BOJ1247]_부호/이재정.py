import sys
input=sys.stdin.readline
result = []

for i in range(3):
    sum = 0
    n = int(input())

    for j in range(n):
        temp = int(input())
        sum += temp

    if sum == 0:
        result.append("0")
    elif sum > 0:
        result.append("+")
    else:
        result.append("-")

for i in result:
    print(i, end="\n")