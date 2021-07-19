import sys
input = sys.stdin.readline
#제곱하면 일의자리 수가 반복된다
li = [[], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
#테스트케이스 갯수 입력
t = int(input())
for i in range(t):
    #a, b입력
    a, b = map(int, input().split())
    #배열 li가 1자리 정수 a랑 b에대해 a^b를 10으로 나눈 나머지를 계산하는 역할인데
    #a가 10보다 클때 a를 10으로 나눠서 b를 제곱한 것의 나머지나 결과가 같아서 마지막 자리를 남기는 처리
    # 가나다 일때 뒤에서 첫자리 (-1)은 다
    a = int(str(a)[-1])
    if a != 0:
        print(li[a][b % len(li[a])])
    else:
        print(10)