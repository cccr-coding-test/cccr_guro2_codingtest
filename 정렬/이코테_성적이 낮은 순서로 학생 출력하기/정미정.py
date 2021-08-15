n = int(input())

array = []
for i in range(n) :
    # 리스트 내 리스트를 삽입
    array.append(input().split())

array = sorted(array, key = lambda x : int(x[1]))

for i in array:
    print(i[0] , end = ' ')