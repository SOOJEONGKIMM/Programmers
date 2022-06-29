def solution(record):
    answer = []
    rec={}
    for one in record:
        read = one.split()
        uid = read[1]
        if len(read)==3:
            name = read[2]
            rec[uid]=name#중복제거

    for one in record:
        res=''
        read = one.split()
        if read[0]=='Enter':
            res+=rec[read[1]]
            res+='님이 들어왔습니다.'
        elif read[0]=='Leave':
            res+=rec[read[1]]
            res+='님이 나갔습니다.'
        if len(res)!=0:
            answer.append(res)

    return answer
