from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        cnt=0
        price = queue.popleft()#비교대상
        for p in queue:
            cnt+=1
            if p < price:#가격 떨어지는 지점 
                break
        answer.append(cnt)
    return answer
