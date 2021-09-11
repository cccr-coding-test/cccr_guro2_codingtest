# youtube 풀이 참조...
from functools import cmp_to_key

def compare(a,b):
    if a[1] == b[1]:
        return a[0] - b[0]
    return b[1] - a[1]

def solution(N, stages):
    answer = []
    total = len(stages)
    fails = []

    users = [0 for _ in range(N+1)]
    for s in stages:
        users[s-1] += 1 #인덱스를 0부터 쓰기 위해

    for i in range(N):
        if users[i] == 0:
            fails.append((i+1, 0))
        else:
            fails.append((i+1, users[i]/total)) #실패율 --> 반환해야 하는 값은 스위치 번호 => 튜플로 묶음
            total -= users[i]

    for f in sorted(fails, key=cmp_to_key(compare)):
        answer.append(f[0])

    return answer
