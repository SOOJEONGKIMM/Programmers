from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        comb = []
        for o in orders:
            comb += combinations(sorted(o),c)
        countered = Counter(comb)
        if len(countered)!=0 and max(countered.values())!=1:
            answer += [''.join(i) for i in countered if countered[i]==max(countered.values())]

    answer.sort()    
    return answer
