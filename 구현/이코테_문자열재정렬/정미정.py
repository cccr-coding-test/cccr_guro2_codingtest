a = input()
abc = list()
num =0

for i in a:
    if i.isalpha():
        abc.append(i)
    else:
        num +=int(i)

abc.sort()
abc.append(num)
for j in abc:
    print(j, end='')

##isalpha() 
