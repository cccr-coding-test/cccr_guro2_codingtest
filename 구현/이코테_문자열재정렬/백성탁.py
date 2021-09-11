S = input()

word = []
num = 0
for i in S:
    if i.isalpha():
        word.append(i)
        word.sort()
    elif i.isdigit():
        num += int(i)

print(''.join(word), num, sep='')