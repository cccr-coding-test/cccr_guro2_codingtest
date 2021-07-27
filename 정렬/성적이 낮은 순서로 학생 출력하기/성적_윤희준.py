N = int(input())
a = []
for i in range(N):
    d = input().split()
    a.append((d[0], int(d[1])))
a = sorted(a, key=lambda student: student[1])
for student in a:
    print(student[0], end = ' ')