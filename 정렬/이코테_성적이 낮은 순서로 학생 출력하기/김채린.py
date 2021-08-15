n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))

def return_score(array):
    return array[1]

students = sorted(students, key=return_score)
for name, score in students:
    print(name, end=" ")