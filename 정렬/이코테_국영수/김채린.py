import sys
input = sys.stdin.readline

# 학생 수
N=int(input())

arr=[]

for i in range(N):
    [name, kor, eng, math] = map(str, input().split())
    arr.append([name, int(kor), int(eng), int(math)])
sorted_arr = sorted(arr, key=lambda x : (-x[1], x[2], -x[3], x[0]))
    
for score in sorted_arr:
    print(score[0])
