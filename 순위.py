from collections import defaultdict

def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    # 경기 결과 입력 받기
    for (winner, loser) in results:
        win[winner].add(loser)
        lose[loser].add(winner)
    # 경기 결과 합치기
    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])
    # 경기 결과가 (n - 1)개면 순위를 정할 수 있음
    for i in range(1, n + 1):
        if (len(win[i]) + len(lose[i])) == (n - 1): answer += 1

    return answer
