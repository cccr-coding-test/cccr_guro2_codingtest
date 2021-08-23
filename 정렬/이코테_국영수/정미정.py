N = int(input())

array = []

for i in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

# sorted 함수의 key 속성
array = sorted(array, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for data in array:
    print(data[0])
    
# lambda는 익숙해지지가 않는다..확인하기
