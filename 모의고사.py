def solution(answers):
    answer = []
    s1=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    s2=[2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    s3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1cnt,s2cnt,s3cnt=0,0,0
    for i,a in enumerate(answers):
        if a==s1[i%10]:
            s1cnt+=1
        if a==s2[i%16]:
            s2cnt+=1
        if a==s3[i%20]:
            s3cnt+=1
    k=max(s1cnt,s2cnt,s3cnt)
    if k==s1cnt:
        answer.append(1)
    if k==s2cnt:
        answer.append(2)
    if k==s3cnt:
        answer.append(3)
    
    return answer

