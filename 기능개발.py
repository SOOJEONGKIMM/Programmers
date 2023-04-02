def solution(progresses, speeds):
    res = []
    days=0
    cnt=0
    while progresses:
        if (progresses[0] + days*speeds[0])>=100:
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if cnt > 0:
                res.append(cnt)
                cnt=0
            days+=1
    res.append(cnt)
    return res
