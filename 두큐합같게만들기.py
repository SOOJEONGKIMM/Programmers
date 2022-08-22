from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum_1=sum(queue1)
    sum_2=sum(queue2)
    dq_1 = deque(queue1)
    dq_2 = deque(queue2)
    for i in range(len(queue1)*3):
        if sum_1>sum_2:
            s=dq_1.popleft()
            dq_2.append(s)
            sum_1-=s
            sum_2+=s
            answer+=1
        elif sum_1<sum_2:
            s=dq_2.popleft()
            dq_1.append(s)
            sum_2-=s
            sum_1+=s
            answer+=1
        else:
            return answer
    return -1
            
 
