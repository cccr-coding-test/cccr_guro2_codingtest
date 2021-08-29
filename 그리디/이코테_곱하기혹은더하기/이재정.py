s = input()
sum = 1

for i in s:
    if i != '0':
        sum *= int(i)

print(sum)