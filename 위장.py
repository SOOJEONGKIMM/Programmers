def solution(clothes):
    answer = 1
    match={}
    for a in clothes:
        if a[1] not in match.keys():
            match[a[1]]=[a[0]]
        else:
            match[a[1]].append(a[0])

    for i, (k, v) in enumerate(match.items()):   
        answer *= len(v)+1
 
    return answer-1
