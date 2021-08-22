n = int(input())

str_n = str(n)
half_len = int(len(str_n)/2)

left_sum, right_sum = 0, 0

for i in range(half_len):
    left_sum += int(str_n[i])

for i in range(half_len, len(str_n)):
    right_sum += int(str_n[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")