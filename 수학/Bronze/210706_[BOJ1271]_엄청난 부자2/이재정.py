n, m = map(int, input().split()) #input 받으면 n, m의 type이 str이기 때문에 map 함수를 통해 int로 변환

print(n//m) #n은 default로 BigDecimal을 지원하지 않기 때문에 n이 매우 큰 정수면 쓰레기값이 출력됨.
            #값을 정수로 반환하는 '//' 연산자를 사용
print(n%m)
