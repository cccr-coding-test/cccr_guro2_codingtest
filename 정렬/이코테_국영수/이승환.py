# N명의 이름과 국어, 영어, 수학 점수 입력
# 국어 점수 내림차순
# 국어 점수 같으면 영어 점수 오름 차순
# 영어 점수 같으면 수학 점수 내림 차순
# 모든 점수 같으면 이름 오름 차순

n = int(input())
data = []

for i in range(n):
    name, score1, score2, score3 = input().split()
    data.append([name, int(score1), int(score2), int(score3)])

# 여러 개의 조건이 있는 정렬은 sorted와 lambda 식으로 해결
data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(data[i][0])
