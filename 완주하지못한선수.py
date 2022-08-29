def solution(participant, completion):
    idxx=0
    participant.sort()
    completion.sort()
    for idx,i in enumerate(participant):
        if len(completion)<idx+1:
            idxx=idx
            break
        elif i !=completion[idx]: 
            idxx=idx
            break
            
    answer=participant[idxx]
        
    return answer
