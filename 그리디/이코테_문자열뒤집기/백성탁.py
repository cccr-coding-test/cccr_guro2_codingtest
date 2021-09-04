S = input()
cnt0, cnt1 = 0, 0

for i in range(len(S)):
    if S[i-1] != S[i]:
        if S[i] == '0':
            cnt1 += 1
        else:
            cnt0 += 1

print(min(cnt0, cnt1))        


