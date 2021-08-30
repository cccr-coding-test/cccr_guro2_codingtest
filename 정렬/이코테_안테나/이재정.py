n, m = map(int, input().split())

matrix = [[0]] * n

direct = [
    [1, 0], [-1, 0], [0, 1], [0, -1]
]

for i in range(n):
    matrix[i] = list(map(int, input().split()))

N = int(input())
data = list(map(int, input().split()))
data.sort()
 
print(data[N//2 - 1])