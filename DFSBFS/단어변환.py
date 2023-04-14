from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin,0])
    visited=[0]*len(words)
    while q:
        word, cnt = q.popleft()
        if word==target:
            answer=cnt
            break
        for i in range(len(words)):
            if not visited[i]:
                tmp_cnt=0
                for j in range(len(words[i])):
                    if words[i][j]!=word[j]:
                        #print(words[i], word)
                        #print(words[i][j],word[j])
                        tmp_cnt+=1                      
                if tmp_cnt==1:
                    #print("matched!",words[i], word)
                    visited[i]=1
                    cnt+=1
                    q.append([words[i], cnt])
                    #break
                    
    
    return answer
