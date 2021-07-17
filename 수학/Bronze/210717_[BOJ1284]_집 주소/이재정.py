result = []

while(True):
    sum = 2
    num = input()
    if num[0] == '0':
        break
    for i in num:
        if i == '1':
            sum += 2
        elif i == '0':
            sum += 4
        else:
            sum += 3
    result.append(sum + len(num) - 1)

for i in result:
    print(i)