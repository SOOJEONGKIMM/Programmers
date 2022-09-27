from collections import defaultdict
def solution(info, query):
    data = dict()
    #data = defaultdict(list)
    for a in ['cpp','java','python','-']:
        for b in ['backend','frontend','-']:
            for c in ['junior','senior','-']:
                for d in ['chicken', 'pizza','-']:
                    data.setdefault((a,b,c,d),list())
    print(data)   
    for i in info:
        i= i.split()
        for a in [i[0], '-']:#언어
            for b in [i[1], '-']:#직군
                for c in [i[2], '-']:#경력
                    for d in [i[3], '-']:#소울푸드
                        data[(a,b,c,d)].append(int(i[4]))#점수
                        
    for k in data:
        data[k].sort()
        
    answer = list()
    for q in query:
        q=q.split()
        pool = data[(q[0],q[2],q[4],q[6])]
        minscore = int(q[7])
        l=0
        r=len(pool)
        mid=0
        while l<r:
            mid=(r+l)//2
            if pool[mid] >= minscore:
                r = mid
            else:
                l = mid+1
        answer.append(len(pool)-l)
                
                        
    return answer
