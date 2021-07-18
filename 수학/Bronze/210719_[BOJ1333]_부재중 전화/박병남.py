# 파이썬 답지 못한 풀이

song_num, song_length, bell_interval = map(int,input().split())
zone, song_zone = -1, -1
flag = True
while flag:
    zone += 1
    song_zone += 1
    if zone>(song_length*song_num+(song_num-1)*5):
        break
    if song_zone==song_length:
        for _ in range(5):
            if zone%bell_interval == 0:
                result1 = zone
                flag = False
                break
            else:
                zone +=1
        zone -= 1
        song_zone = -1

if flag:
    while True:
        if zone % bell_interval == 0:
            result2=zone
            break
        zone += 1
    print(result2)
else:
    print(result1)
