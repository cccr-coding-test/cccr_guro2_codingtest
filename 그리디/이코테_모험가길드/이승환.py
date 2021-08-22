# 그리디: 현재 상황에서 특정한 기준에 따라 가장 좋아 보이는 것만을 선택
# 모험가 N명 대상으로 공포도 측정
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여
# 최대 몇 개의 모험가 그룹을 만들 수 있는지?
n = int(input())
x = list(map(int, input().split()))

x.sort() 

group = 0    
party = 0
 
for i in x:
    party += 1
    # 파티 인원수가 공포도 이상이면 그룹 증가
    if party >= i:
        party = 0
        group += 1

print(group)