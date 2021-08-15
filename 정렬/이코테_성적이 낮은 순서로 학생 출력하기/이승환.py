from array import array
from os import rename


n = int(input())
array = []

for i in range(n):
    name, score = input().split()
    array.append((name, score))

# 키를 이용하여 점수를 기준으로 정렬
# 망할 lambda식: key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬, -를 붙이면 현재 정렬차순과 반대로
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')