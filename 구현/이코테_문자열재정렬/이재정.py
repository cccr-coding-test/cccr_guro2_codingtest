s = input()
arr= []
sum = 0

for i in s:
    arr.append(i)

arr.sort()

for i in arr:
    if i >= '0' and i <= '9':
        sum += int(i)
    else:
        print(i, end="")

print(sum)