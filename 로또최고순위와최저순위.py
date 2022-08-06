def solution(lottos, win_nums):
    answer = []
    count = 0
    rank = [6,6,5,4,3,2,1]
    zerocount=lottos.count(0)
    for i in lottos:
        if i==0:
            count+=1
        elif i in win_nums:
            count+=1

    answer = [rank[count], rank[count-zerocount]]
    
    
    
    return answer
