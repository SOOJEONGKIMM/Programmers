def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    link = set([costs[0][0]])#start
    
    #Kruskal
    while len(link)!=n:
        for v in costs:
            if v[0] in link and v[1] in link: #이미 추가된 낮은 가격있으면 패스   
                continue
            elif v[0] in link or v[1] in link:
                answer+=v[2]
                link.update([v[0],v[1]])
                print([v[0],v[1]],link)
                break
                
                
    return answer
