
ss=input()

old_s=ss[0]
block_0,block_1=0,0


if old_s=='0':
    block_0+=1
else:
    block_1+=1
for s in ss:
    if old_s!=s:
        if s=='1':
            block_1+=1
        else:
            block_0+=1
        old_s=s

print(min(block_0,block_1))
