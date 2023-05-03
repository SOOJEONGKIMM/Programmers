def solution(s):
    answer = 0
 
    '''
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j]==s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))
       '''
 
    
    return len(s) if s[::-1]==s else max(solution(s[:-1]), solution(s[1:]))
