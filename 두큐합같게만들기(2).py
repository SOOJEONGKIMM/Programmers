from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total_sum = (sum1 + sum2) // 2
    q1 = deque(queue1)
    q2 = deque(queue2)

    while q1 and q2:
        if sum1 > total_sum:
            tmp = q1.popleft()
            #q2.append(tmp)
            answer+=1
            sum1 -= tmp
            
        elif sum1 < total_sum:
            tmp = q2.popleft()
            q1.append(tmp)
            answer+=1
            sum1 += tmp
            
        elif sum1 == total_sum:
            return answer
    return -1 
