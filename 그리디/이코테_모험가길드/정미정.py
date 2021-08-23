n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
count = 0

for i in range(len(arr)):
    val = arr[i]
    count += 1
    if val == count:
        result += 1
        count = 0
        
print(result)
