from collections import deque
def solution(n, edge):
    answer = 0
    visit = [0]*(n+1)
    adj=[[] for _ in range(n+1)]
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
    queue = deque([1])
    visit[1]=1
    while queue:
        x = queue.popleft()
        for next in adj[x]:
            if not visit[next]:
                queue.append(next)
                visit[next] = visit[x]+1
                
    answer = visit.count(max(visit))
    
    return answer
