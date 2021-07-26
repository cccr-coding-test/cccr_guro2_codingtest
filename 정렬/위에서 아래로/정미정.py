# 반복할 수 n 입력
n = int(input())
arr =[]

for i in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse=True) #reverse=True는 내림차순
for i in range(n):
    print(arr[i], end=" ")


# sorted()는 리스트를 반환, 리스트 외에 딕셔너리등 모든 이터러블 가능
# sort()는 none을 반환, 리스트만 가능