n = int(input())

result = []
for i in range(n):
  temp = int(input())
  result.append(temp)

result.sort(reverse=True)
print(result)

