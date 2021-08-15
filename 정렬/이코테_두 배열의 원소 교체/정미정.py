n ,k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a) # a.sort()
b = sorted(b, reverse=True) # b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i],a[i]
    else:
        break
        # 정렬한 상태라 a의 원소가 b의 원소보다 크거나 같으면 더 비교하지 않아도 됨

print(sum(a))

#python은 swap 안 써도 됨
# n은 입력받고 안쓰네...