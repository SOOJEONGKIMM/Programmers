from collections import Counter
def solution(N, stages):
    answer = []
    fail = {}
    stages.sort()
    c_s = Counter(stages)
    for i in range(N):
        if i+1 not in stages:
            c_s[i+1]=0
    c_s = dict(sorted(c_s.items(),key = lambda i: i[0]))

    k = list(c_s.keys())
    v = list(c_s.values())

    for i in range(N):
        print(i+1,k[i])
        if i+1 in stages:
            fail[i+1]=v[i]/sum(v[i:])
        else:
            fail[i+1]=0
    fail=sorted(fail.items(), key=lambda pair: pair[1], reverse=True)
    for ke,va in fail:
        answer.append(ke)

    return answer
