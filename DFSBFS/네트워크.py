from collections import deque
def solution(n, computers):
    answer = 0
    visited=[0]*n
    def bfs(node, visited):
        queue = deque()
        queue.append(node)
        visited[node]=1
        while queue:
            x = queue.popleft()
            for i in range(n):        
                if computers[x][i]==1 and not visited[i]:
                    visited[i]=1
                    queue.append(i)
            
    for node in range(n):
        if not visited[node]:
            bfs(node, visited)
            answer+=1
    
    return answer
