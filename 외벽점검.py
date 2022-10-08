def solution(n, weak, dist):
    answer = 0
    di = sorted(dist, reverse=True)
    repair_lst = [()]
    for d in di: #큰애들부터 차례대로 
        answer+=1
        repaired = []
        for idx, w in enumerate(weak):
            start = w
            end = weak[idx:] +[n+w for w in weak[:idx]] #슬라이딩윈도우 탐색
            can = [e%n for e in end if e-start <= d] #end에서 가능한애들 뽑아내기 
            repaired.append(set(can))
        cand = set()
        for r in repaired: #그전 반복문에서 구한 애들이랑 합치기
            for l in repair_lst:
                new = r | set(l) #합집합 OR
                if len(new) == len(weak):
                    return answer 
                cand.add(tuple(new))
        repair_lst = cand 
    return -1
