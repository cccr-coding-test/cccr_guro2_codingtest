def solution(s):
    answer = 0
    cnt = len(s)
    for i in range(1,len(s)//2+1):
        li = []
        for j in range(0,len(s),i):
            if not li:
                li.append([s[j:j+i],1])
            else:
                if li[-1][0]!=s[j:j+i]:
                    li.append([s[j:j+i],1])
                else:
                    li[-1][1] +=1
                    
        chk = 0
        for k in li:
            if k[1]!=1:
                chk+=len(str(k[1]))
                # chk+=1
            chk+=len(k[0])
        cnt = min(cnt,chk)
        
    return cnt
