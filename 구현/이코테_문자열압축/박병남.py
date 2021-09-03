def solution(s):
    len_s=len(s)
    answer=len_s
    for i in range(1,len_s//2+1):
        temp_s=s[:i]
        temp_cnt=1
        temp_answer=""
        for j in range(i,len_s,i):
            if temp_s==s[j:i+j]:
                temp_cnt+=1
            else:
                if temp_cnt==1:
                    temp_cnt=""
                temp_answer+=str(temp_cnt)+temp_s
                temp_s=s[j:i+j]
                temp_cnt=1

        if temp_cnt==1:
            temp_cnt=""
        temp_answer+=str(temp_cnt)+temp_s
        answer=min(answer,len(temp_answer))
    return answer
