ss=input()
str=[]
dem=[]
for s in ss:
    if ord('0') <= ord(s) <=ord('9'):
        dem.append(int(s))
    else:
        str.append(s)

str.sort()
for i in str:
    print(i,end='')
print(sum(dem))
