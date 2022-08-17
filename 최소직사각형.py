def solution(sizes):
    answer = 1000001
    x,y=[],[]
    for i in range(len(sizes)):
        if sizes[i][0]>=sizes[i][1]:
            x.append(sizes[i][0])
            y.append(sizes[i][1])
        else:
            y.append(sizes[i][0])
            x.append(sizes[i][1])
    
    answer=max(x)*max(y)
        
    
    
    return answer
