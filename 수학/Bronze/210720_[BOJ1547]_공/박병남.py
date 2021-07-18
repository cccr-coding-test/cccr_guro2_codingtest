# 가볍게 생각난대로 풀기
mylist = []
key = 1
for _ in range(int(input())):
    mylist.append(list(map(int,input().split())))
for my in mylist:
    if key in my:
        my.remove(key)
        key=my[0]
print(key)


# 버블정렬 응용해서 풀기
cups = [0,1,0,0]
for i in range(int(input())):
    c1,c2 = map(int,input().split())
    cups[c1],cups[c2] = cups[c2],cups[c1]
print(cups.index(1))
