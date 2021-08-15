n = int(input())
info = {}

for i in range(n):
  name, score = input().split()
  score = int(score)
  info[name] = score

sorted_info = sorted(info.items(), key=lambda x: x[1])

for key, value in sorted_info:
  print(key, end=" ")
