s = input()
result = 0
for i in s:
    if result == 0:
        result += int(i)
    elif int(i) == 1:
        result += int(i)
    else:
        result *= int(i)
print(result)
