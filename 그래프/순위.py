from collections import defaultdict
def solution(n, results):
    answer = 0
    winner = defaultdict(set)
    loser = defaultdict(set)
    for win, lose in results:
        winner[win].add(lose)
        loser[lose].add(win)
    #합치기
    for i in range(1,n+1):
        for win in loser[i]:
            winner[win].update(winner[i])
        for lose in winner[i]:
            loser[lose].update(loser[i])
   
    for i in range(n+1):
        if len(loser[i])+len(winner[i])==n-1:
            answer+=1
    return answer
