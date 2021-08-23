n = int(input())
student = []

for i in range(n):
    temp = list(input().split())
    student.append(temp)

student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
    print(i[0])