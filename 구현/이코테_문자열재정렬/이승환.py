s = input()
data = []
num = 0

for i in s:
    if i.isalpha():
        data.append(i)
    else:
        num += int(i)

data.sort()
data.append(num)

for i in data:
    print(i,end='')