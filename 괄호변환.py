def divide(w):
    left=0
    right=0
    for i in range(len(w)):
        if w[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:#균형잡힌 괄호문자열 
            return w[:i+1], w[i+1:]

        
def isbalanced(u):#올바른 괄호문자열인지 
    stack = []
    for i in u:
        if i=='(':
            stack.append(i)
        else: 
            if not stack:
                return False
            stack.pop() 
    return True



def solution(p):
    answer = ''
    if not p:
        return ""
    u, v = divide(p)
    if isbalanced(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        
        
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    
    return answer

