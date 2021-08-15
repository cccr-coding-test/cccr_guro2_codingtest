a=input()
half=len(a)//2
head_total, rear_total = 0, 0

for i in range(half):
    head_total+=int(a[i])
    j=i+half
    rear_total+=int(a[j])

if head_total==rear_total:
    print("LUCKY")
else:
    print("READY")
    
    
# 혹은

a=input()
half=len(a)//2
heads,rears=a[:half],a[half:]
head_total, rear_total = 0, 0

for i in range(half):
    head_total+=int(heads[i])
    rear_total+=int(rears[i])

if head_total==rear_total:
    print("LUCKY")
else:
    print("READY")
