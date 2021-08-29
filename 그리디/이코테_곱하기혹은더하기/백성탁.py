N = input()
result = 0

for i in N:
    if result == 0 or int(i) <= 1:
        result += int(i)
    else:
        result *= int(i)

print(result)
