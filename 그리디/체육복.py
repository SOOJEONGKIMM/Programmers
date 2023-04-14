def solution(n, lost, reserve):
    answer = 0
    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    if len(set_lost)==0:
        answer = n
    else:
        answer = n - len(set_lost)
        #print(set_reserve, set_lost)
    return answer
