
def solution(info, edges):
    answer = []
    visited = [0]*len(info)
    visited[0]=1
    def dfs(s_cnt, w_cnt):
        if s_cnt <= w_cnt:
            return
        else:
            answer.append(s_cnt)
        for a,b in edges:
            if visited[a] and not visited[b]:
                visited[b]=1
                whoischild = info[b]
                dfs(s_cnt+(whoischild==0),w_cnt+(whoischild==1))  
                visited[b]=0
    dfs(1,0)
    return max(answer)
