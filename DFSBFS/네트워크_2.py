from collections import deque
def solution(n, computers):
    answer = 0
    visited=[0]*n
    q = deque()
    def dfs(node, visited):
        q.append(node)
        while q:
            x = q.popleft()
            for i in range(n):
                if not visited[i] and computers[x][i]==1:
                    visited[i]=1
                    q.append(i)
        
    for i in range(n):
        if not visited[i]:
            visited[i]=1
            dfs(i, visited)
            answer+=1
            
    return answer
