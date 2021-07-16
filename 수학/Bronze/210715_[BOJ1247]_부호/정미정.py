import sys

for i in range(3):
    li = []
    for j in range(int(sys.stdin.readline())):
        li.append(int(sys.stdin.readline()))

    if sum(li) > 0:
        print("+")
    elif sum(li) < 0:
        print("-")
    else:
        print("0")
