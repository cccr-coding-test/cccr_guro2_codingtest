#bisect_right(), bisect_left() 메소드를 사용하면
#첫번째 인자의 배열에 두번째 요소를 집어넣을 때 각각 오른쪽, 왼쪽에서 넣을 경우
#몇 번째 인자에서 넣어야 하는지를 반환해줌.

import bisect

n, x = map(int, input().split())
num = sorted(list(map(int, input().split())))
cnt = bisect.bisect_right(num, x) - bisect.bisect_left(num, x)

if cnt < 0:
    print(-1)
else:
    print(cnt)