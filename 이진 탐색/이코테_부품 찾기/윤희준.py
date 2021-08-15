n = int(input())
a = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in a:
        print('yes',end= ' ')
    else:
        print('no', end=' ')

# 책참고,,
