A, B, C = map(int, input().split())
braek_even_point = int(A/(C-B)+1)
if braek_even_point >= 0:
    print(braek_even_point)
else:
    print("-1")