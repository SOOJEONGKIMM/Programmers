def solution(new_id):
    answer = ''
    fine = ['0','1','2','3','4','5','6','7','8','9','-','_','.']
    dot='.'
    cnt=0
    for i in new_id:
        one=new_id[cnt]
        if ord(i)>=97 and ord(i)<=122:
            good=0
        elif ord(i)>=65 and ord(i)<=90:
            i = chr(ord(i)+32)
        elif i not in fine:
            i=''
        
        if cnt<len(new_id)-1:        
            two=new_id[cnt+1]
            if one==dot and two==dot:
                i=''
            cnt+=1
        answer+=i
       
    tmp=answer
    answer=''
    cnt=0
    for i in tmp:
        one=tmp[cnt]
        if cnt<len(tmp)-1:        
            two=tmp[cnt+1]
            if one==dot and two==dot:
                i=''
            cnt+=1
        answer+=i
    while answer[0]=='.':
        if len(answer)>1:
            answer = answer[1:]
        else: break
    while answer[-1]=='.':
        if len(answer)>1:
            answer = answer[:-1]
        else: break
    if len(answer)==0 or answer=='.':
        answer='a'#*len(new_id)
    elif len(answer)>=16:
        answer = answer[:15]
        while answer[-1]=='.':
            if len(answer)>1:
                answer = answer[:-1]
            else: break
    if len(answer)<=2:
        while len(answer)<3:
            answer += answer[-1]
    return answer
