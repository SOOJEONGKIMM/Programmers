'''시간초과 코드
from itertools import combinations
def solution(number, k):
    answer = 0
    for c in list(combinations(number,len(number)-k)):
        tmp=''.join(c)
        answer=max(answer,int(tmp))
    return str(answer)
'''


def solution(number, k):
    answer = []
    for n in number:
        if not answer:
            answer.append(n)
            continue
        if k>0:
            while answer[-1]<n:
                answer.pop()
                k-=1
                if not answer or k<=0:
                    break
        answer.append(n)
    answer = answer[:-k] if k>0 else answer
    return ''.join(answer)
