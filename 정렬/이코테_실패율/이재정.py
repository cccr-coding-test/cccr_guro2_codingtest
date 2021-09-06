def solution(n, stages):
    fail = {}
    cnt = 0
    tmp = len(stages)
    result = []

    for i in range(n):
        len_stages = tmp - cnt
        cnt = 0
        for j in stages:
            if i+1 == j:
                cnt += 1
        if cnt == 0:
            fail[i+1] = 0
        else:
            fail[i+1] = cnt/len_stages
        tmp = len_stages

    sorted_value = sorted(fail.items(), key=lambda x:x[1], reverse=True)

    for i in sorted_value:
        result.append(i[0])

    return result

n = int(input())
stages = list(map(int, input().split()))
solution(n, stages)