#아스키=>문자열 chr()    문자열=>아스키 ord()

n=input()

y=ord(n[0])
x=int(n[1])

pos_list=[[-2,-1],[-2,1],[2,-1],[2,1],[1,2],[1,-2],[-1,2],[-1,-2]]
result=0

for i in pos_list:
    mov_x=x-i[0]
    mov_y=y-i[1]
    if 1<=mov_x<=8 and ord('a')<= mov_y <=ord('h'):
        result +=1

print(result)