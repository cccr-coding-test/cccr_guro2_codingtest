a = input()
num = 0

for i in a:
    if i ==('1' or '0') or num <=1:
        num +=int(i)
    else:
        num *=int(i)

print(num)
