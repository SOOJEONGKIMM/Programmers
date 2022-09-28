def solution(play_time, adv_time, logs):
    c = lambda x: int(x[:2])*3600 + int(x[3:5])*60 + int(x[6:])
    play, adv = c(play_time)+1, c(adv_time)
    sec_arr = [0]*play
    #logs = sorted([s for t in logs for s in [(c(t[:8]),1), c(t[9:]),0]])
    print(play)
    for l in logs:
        start = c(l[:8])
        end = c(l[9:])
        sec_arr[start]+=1
        sec_arr[end]-=1
        
    for idx in range(1, play):
        sec_arr[idx] += sec_arr[idx-1] #누적합
        
    st=0
    ans_cnt = cnt = sum(sec_arr[:adv])
    ans_str=0
    for en in range(adv, play):
        cnt-=sec_arr[st]
        st+=1
        cnt+=sec_arr[en]
        
        if ans_cnt < cnt:
            ans_cnt = cnt
            ans_str = st
            
    print(ans_str)
    
    #return answer
