def solution(tickets):
    answer = []
    visited = [0]*(len(tickets)+1)
    
    def dfs(land, path):

        if len(path)==(len(tickets)+1):
            answer.append(path)
        for idx, ticket in enumerate(tickets):
            if visited[idx]==0 and ticket[0]==land:
                visited[idx]=1
                dfs(ticket[1], path+[ticket[1]])
                visited[idx]=0
                
                
    dfs("ICN",["ICN"])
    return sorted(answer)[0]
