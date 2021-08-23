N = input()
length = len(N)
sum = 0

for i in range(length // 2):
    sum += int(N[i])

for i in range(length // 2, length):
    sum -= int(N[i])

if sum == 0:
    print("LUCKY")
else:
    print("READY")