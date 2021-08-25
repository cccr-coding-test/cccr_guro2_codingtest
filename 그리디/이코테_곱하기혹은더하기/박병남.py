s=input()
mylist=list()
for i in s:
    mylist.append(int(i))

result=mylist[0]
for my in mylist[1:]:
    if result==0:
        result+=my
    else:
        result*=my

print(result)
