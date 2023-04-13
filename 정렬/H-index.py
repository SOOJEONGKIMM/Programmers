def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    for idx, c in enumerate(citations):
        if n-idx <= c:
            answer = n-idx
            break
    return answer
