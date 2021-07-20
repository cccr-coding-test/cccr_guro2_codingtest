P, K = map(int, input().split())
l = [1]*K
for i in range(2, int(K**0.5)+1):
    if l[i] == 1:
        for j in range(i+i, K, i):
            l[j] = 0
prime = [i for i in range(2, K) if l[i] == 1]

good, bad = 1, 0
for n in prime:
    if P%n == 0:
        good, bad = 0, n
        break
print("GOOD" if good else f"BAD {bad}")

# 에라토스테네스의 체 확인..필요...