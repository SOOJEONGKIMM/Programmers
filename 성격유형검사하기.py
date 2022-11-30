def solution(survey, choices):
    answer = ''
    base={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    mbti=dict()
    c_list = [1,2,3,4,5,6,7]
    p_list = [3,2,1,0,1,2,3]
    mbti = dict()
    d = dict(zip(c_list,p_list))
    
    for s, c in zip(survey, choices):
        if c < 4:
            try:
                mbti[s[0]]+=d[c]
            except:
                mbti[s[0]]=d[c]
        else:
            try:
                mbti[s[1]]+=d[c]
            except:
                mbti[s[1]]=d[c]
    for k, v in base.items():
        try:
            mbti[k]+=0
        except:
            mbti[k]=0
    
    answer+="R" if mbti["R"]>=mbti["T"] else "T"
    answer+="C" if mbti["C"]>=mbti["F"] else "F"
    answer+="J" if mbti["J"]>=mbti["M"] else "M"
    answer+="A" if mbti["A"]>=mbti["N"] else "N"
    return answer
