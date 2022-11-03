
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=deque([0]*bridge_length)
    trucks = deque(truck_weights)
    bridge_sum=0
    while bridge:
        p = bridge.popleft()
        bridge_sum-=p
        if trucks:
            if bridge_sum+trucks[0] <= weight:
                t = trucks.popleft()
                bridge.append(t)
                bridge_sum+=t
            else:
                bridge.append(0)
                    
        answer+=1
    
    return answer 

