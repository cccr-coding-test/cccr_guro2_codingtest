mylist=[]
for _ in range(int(input())):
    mylist.append(int(input()))

mylist.sort(reverse=True)

for my in mylist:
  print(my,end=' ')
